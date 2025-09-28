from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import os

# Caminho para o arquivo de credenciais
creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")

# Autenticação
creds = Credentials.from_service_account_file(creds_path)
service = build('drive', 'v3', credentials=creds)

# Teste: liste as pastas
results = service.files().list(
    q="mimeType='application/vnd.google-apps.folder'",
    fields="files(id, name)"
).execute()

files = results.get('files', [])

if not files:
    print("Nenhuma pasta encontrada.")
else:
    print("Pastas encontradas:")
    for file in files:
        print(f"Nome: {file['name']}, ID: {file['id']}")