from crewai.tools import BaseTool

class CurrencyConverterTool(BaseTool):
    name: str = "Conversor de Moedas"
    description: str = (
        "Converte valores de USD para EUR ou BRL usando taxas de câmbio simuladas. "
        "Use quando o usuário pedir valores em moeda local. "
        "Formato de entrada: '1000 USD to EUR' ou '500 USD to BRL'."
    )

    def _run(self, query: str) -> str:
        # Simula taxas de câmbio (você pode substituir por uma API real depois)
        rates = {
            "EUR": 0.93,
            "BRL": 5.10
        }

        try:
            parts = query.strip().split(" ")
            if len(parts) != 4 or parts[1].upper() != "USD" or parts[2].lower() != "to":
                return "Formato inválido. Use: '<valor> USD to <EUR|BRL>'"

            amount = float(parts[0])
            target_currency = parts[3].upper()

            if target_currency not in rates:
                return f"Moeda {target_currency} não suportada. Use EUR ou BRL."

            converted = amount * rates[target_currency]
            return f"{amount} USD = {converted:.2f} {target_currency}"

        except Exception as e:
            return f"Erro na conversão: {str(e)}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Conversão assíncrona não suportada.")