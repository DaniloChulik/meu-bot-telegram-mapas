import os
import requests # Você já tem essa biblioteca instalada

# ----- COLOQUE SEU TOKEN MAIS RECENTE AQUI DIRETAMENTE PARA TESTE -----
# Substitua pela string do token que o BotFather te deu mais recentemente
# Exemplo: TEST_TOKEN = "1234567890:ABCDEFGabcdefgHIJKLMNOPqrstuvWXYZ12345"
TEST_TOKEN = "7656877931:AAGM80OnUerfpIFfGCEEMjajYvNTtneuBrQ"
# --------------------------------------------------------------------

def check_telegram_token(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    try:
        response = requests.get(url, timeout=10)
        print(f"URL da requisição: {url}")
        print(f"Status da Resposta: {response.status_code}")
        print("Resposta JSON:")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("Não foi possível decodificar a resposta como JSON.")
            print("Conteúdo da Resposta (texto):")
            print(response.text)

        if response.status_code == 200 and response.json().get("ok"):
            print("\n>>> TOKEN VÁLIDO! <<<")
            print(f"Nome do Bot: {response.json()['result']['first_name']}")
            print(f"Username do Bot: @{response.json()['result']['username']}")
        else:
            print("\n>>> TOKEN INVÁLIDO OU ERRO NA REQUISIÇÃO! <<<")
            if response.json() and "description" in response.json():
                print(f"Descrição do erro do Telegram: {response.json()['description']}")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao tentar verificar o token: {e}")

if __name__ == "__main__":
    print(f"Testando o token: '{TEST_TOKEN}'")
    if not TEST_TOKEN:
        print("ERRO: O token de teste não foi definido no script.")
    else:
        check_telegram_token(TEST_TOKEN)