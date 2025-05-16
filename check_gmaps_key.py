import googlemaps
import os

# ----- COLOQUE SUA CHAVE DA API DO GOOGLE MAPS DIRETAMENTE AQUI PARA TESTE -----
# Substitua pela string da chave que você está tentando usar
# Exemplo: TEST_GMAPS_API_KEY = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXX"
TEST_GMAPS_API_KEY = "AIzaSyDoDuV1dpZW41apIdTMYFsXr5ZZS4X2hsU" # SUA CHAVE REAL AQUI
# --------------------------------------------------------------------------------

def check_google_maps_key(api_key):
    # A condição abaixo não será mais atingida se você substituiu a chave acima
    if not api_key or api_key == "SUA_CHAVE_GOOGLE_MAPS_AQUI":
        print("ERRO: A chave da API do Google Maps (TEST_GMAPS_API_KEY) não foi definida corretamente no script.")
        print("Por favor, edite o arquivo check_gmaps_key.py e substitua 'SUA_CHAVE_GOOGLE_MAPS_AQUI' pela sua chave real.")
        return

    print(f"Tentando inicializar o cliente Google Maps com a chave: '{api_key[:5]}...{api_key[-5:]}' (parcial para segurança)")

    try:
        gmaps = googlemaps.Client(key=api_key)
        print("Cliente Google Maps inicializado com sucesso (passo 1 - instanciação).")

        # Tenta fazer uma chamada simples de geocodificação
        # (requer que a Geocoding API esteja ativada no seu projeto GCP)
        print("Tentando fazer uma chamada de teste para Geocoding API (ex: 'Googleplex')...")
        geocode_result = gmaps.geocode('Googleplex')

        if geocode_result:
            print("Chamada de Geocoding API bem-sucedida!")
            print(f"Endereço formatado encontrado: {geocode_result[0]['formatted_address']}")
            print("\n>>> CHAVE DA API DO GOOGLE MAPS PARECE VÁLIDA E FUNCIONAL PARA GEOCODING! <<<")
        else:
            print("Chamada de Geocoding API retornou um resultado vazio, mas sem erro de chave.")
            print("Isso pode indicar um problema com a chamada em si, ou a Geocoding API não está habilitada/restringida corretamente.")
            print("Verifique se a 'Geocoding API' está ativa no seu projeto GCP e permitida pela chave.")
            print("\n>>> A CHAVE PODE SER VÁLIDA, MAS O TESTE DE GEOCODING NÃO FOI CONCLUSIVO. <<<")


    except googlemaps.exceptions.ApiError as api_err:
        print(f"\n!!! ERRO DA API DO GOOGLE MAPS !!!")
        print(f"Mensagem: {api_err}")
        if hasattr(api_err, 'status'):
            print(f"Status da API: {api_err.status}")
        print("Causas comuns: chave inválida, API não habilitada no projeto, problemas de faturamento, restrições da chave.")
        print("Verifique suas configurações no Google Cloud Console.")
    except Exception as e:
        print(f"\n!!! OCORREU UM ERRO INESPERADO AO USAR A CHAVE DO GOOGLE MAPS !!!")
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()

# Este bloco executa a função quando o script é rodado
if __name__ == "__main__":
    key_to_test = TEST_GMAPS_API_KEY
    check_google_maps_key(key_to_test)