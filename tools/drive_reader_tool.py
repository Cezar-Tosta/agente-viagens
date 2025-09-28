from crewai.tools import BaseTool
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os

class DriveReaderTool(BaseTool):
    name: str = "Leitor de Arquivos do Google Drive"
    description: str = (
        "Lê arquivos de uma pasta específica do Google Drive e retorna o conteúdo. "
        "Use o ID da pasta do Google Drive."
    )

    def _run(self, folder_id: str) -> str:
        # Caminho para o arquivo de credenciais
        creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")

        # Autenticação
        creds = Credentials.from_service_account_file(creds_path)
        service = build('drive', 'v3', credentials=creds)

        # Listar arquivos na pasta
        results = service.files().list(
            q=f"'{folder_id}' in parents",
            fields="files(id, name, mimeType)"
        ).execute()

        files = results.get('files', [])
        content = []

        for file in files:
            file_id = file['id']
            file_name = file['name']
            mime_type = file['mimeType']

            # Lê o conteúdo do arquivo com base no tipo
            if mime_type == 'application/vnd.google-apps.document':
                # Lê documentos do Google Docs
                doc_content = service.files().export(fileId=file_id, mimeType='text/plain').execute()
                content.append(f"Documento: {file_name}\n{doc_content.decode('utf-8')}")
            elif mime_type == 'application/pdf':
                # Lê PDFs
                request = service.files().get_media(fileId=file_id)
                pdf_content = request.execute()
                content.append(f"PDF: {file_name}\nConteúdo não extraído (binário).")
            else:
                content.append(f"Arquivo: {file_name} (tipo: {mime_type})")

        return "\n\n".join(content)

    async def _arun(self, folder_id: str) -> str:
        raise NotImplementedError("Método assíncrono não suportado.")