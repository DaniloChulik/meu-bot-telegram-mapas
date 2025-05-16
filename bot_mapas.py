# ==============================================================================
# 1. BLOCO DE IMPORTAÇÕES
# ==============================================================================
import json
import requests
import pytz
import random
import re
import os
from dotenv import load_dotenv # Para carregar o .env
from datetime import datetime
from urllib.parse import quote

from telegram import Update, constants as telegram_constants
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters as telegram_filters
import googlemaps # <<< ESTA LINHA PRECISA ESTAR AQUI E DESCOMENTADA

# Carrega variáveis do arquivo .env para o ambiente
load_dotenv()

# ==============================================================================
# 2. CONFIGURAÇÕES DE API E VARIÁVEIS GLOBAIS
# ==============================================================================
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
API_KEY_GOOGLE_MAPS = os.environ.get('API_KEY_GOOGLE_MAPS')

# ... (resto das verificações e inicialização do gmaps_client)
# try:
#     gmaps_client = googlemaps.Client(key=API_KEY_GOOGLE_MAPS)
# except Exception as e:
# print(f"Erro ao inicializar o cliente Google Maps: {e}")
# exit()
# ...

# ==============================================================================
# 2. CONFIGURAÇÕES DE API E VARIÁVEIS GLOBAIS
# ==============================================================================
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
API_KEY_GOOGLE_MAPS = os.environ.get('API_KEY_GOOGLE_MAPS')

if not TELEGRAM_BOT_TOKEN:
    print("ERRO CRÍTICO: Variável de ambiente TELEGRAM_BOT_TOKEN não definida (verifique .env ou ambiente).")
    exit()
# ... (resto do código como antes, usando TELEGRAM_BOT_TOKEN e API_KEY_GOOGLE_MAPS)

# ==============================================================================
# 2. CONFIGURAÇÕES DE API E VARIÁVEIS GLOBAIS - COM TOKENS/CHAVES DIRETOS
# ==============================================================================

# !!!!!!!!!! COLOQUE SEUS TOKENS/CHAVES REAIS E VÁLIDOS AQUI !!!!!!!!!!
# Use o token do Telegram que funcionou no check_token.py
TOKEN_TELEGRAM_DIRETO = "7656877931:AAGM80OnUerfpIFfGCEEMjajYvNTtneuBrQ" # <--- SUBSTITUA SE NECESSÁRIO PELO SEU TOKEN TELEGRAM VÁLIDO
# Use a chave do Google Maps que funcionou no check_gmaps_key.py
API_KEY_GOOGLE_MAPS_DIRETO = "AIzaSyDoDuV1dpZW41apIdTMYFsXr5ZZS4X2hsU" # <--- SUBSTITUA PELA SUA CHAVE GOOGLE MAPS VÁLIDA
# !!!!!!!!!! CERTIFIQUE-SE DE QUE ESTES SÃO OS VALORES CORRETOS !!!!!!!!!!


# Verificações para os tokens/chaves diretas
if not TOKEN_TELEGRAM_DIRETO or TOKEN_TELEGRAM_DIRETO == "SEU_TOKEN_PLACEHOLDER_AQUI": # Ajuste o placeholder se usar um diferente
    print("ERRO CRÍTICO: TOKEN_TELEGRAM_DIRETO não definido corretamente no código com um valor real.")
    exit()

if not API_KEY_GOOGLE_MAPS_DIRETO or API_KEY_GOOGLE_MAPS_DIRETO == "SUA_CHAVE_PLACEHOLDER_AQUI": # Ajuste o placeholder se usar um diferente
    print("ERRO CRÍTICO: API_KEY_GOOGLE_MAPS_DIRETO não definida corretamente no código com um valor real.")
    exit()

# Inicialize o cliente do Google Maps
try:
    gmaps_client = googlemaps.Client(key=API_KEY_GOOGLE_MAPS_DIRETO) # USA A CHAVE DIRETA
    print("INFO: Cliente Google Maps inicializado com chave direta.")
except Exception as e:
    print(f"Erro ao inicializar o cliente Google Maps com chave direta: {e}")
    exit()

# Dicionários e Listas Globais
estado_para_sigla = {
    "State of Acre": "AC", "State of Alagoas": "AL", "State of Amapá": "AP", "State of Amazonas": "AM",
    "State of Bahia": "BA", "State of Ceará": "CE", "State of Espírito Santo": "ES", "State of Goiás": "GO",
    "State of Maranhão": "MA", "State of Mato Grosso": "MT", "State of Mato Grosso do Sul": "MS",
    "State of Minas Gerais": "MG", "State of Pará": "PA", "State of Paraíba": "PB", "State of Paraná": "PR",
    "State of Pernambuco": "PE", "State of Piauí": "PI", "State of Rio de Janeiro": "RJ",
    "State of Rio Grande do Norte": "RN", "State of Rio Grande do Sul": "RS", "State of Rondônia": "RO",
    "State of Roraima": "RR", "State of Santa Catarina": "SC", "State of São Paulo": "SP",
    "State of Sergipe": "SE", "State of Tocantins": "TO", "Federal District": "DF",
}

mensagens_seguranca = [
    "🚗 Use sempre o cinto de segurança.", "🚧 Mantenha distância segura do veículo à frente.",
    "📵 Celular e direção não combinam.", "⚠️ Respeite os limites de velocidade.",
    "🛑 Pare sempre na faixa de pedestres.", "🚦 Sinal vermelho significa pare!",
    "🔍 Faça revisões periódicas no seu veículo.", "🌧️ Em dias de chuva, reduza a velocidade.",
    "🕒 Respeite o tempo de descanso na direção.", "🍺 Se beber, não dirija.",
    "🚘 Olhe sempre os espelhos retrovisores.", "🚚 Cuidado ao ultrapassar caminhões.",
    "🛣️ Atenção redobrada em rodovias.", "🧯 Verifique os itens de segurança do veículo.",
    "🛞 Calibre os pneus regularmente.", "🔧 Faça manutenção preventiva do carro.",
    "📵 Evite distrações enquanto dirige.", "🚙 Ligue os faróis, mesmo de dia, na estrada.",
    "🚸 Redobre a atenção em áreas escolares.", "🦺 Use triângulo de sinalização em emergências.",
    "🚫 Não force ultrapassagens perigosas.", "🛑 Respeite a sinalização da via.",
    "⚙️ Engate a marcha ao estacionar em descidas.", "📛 Dirija com atenção perto de ciclistas.",
    "🛑 Nunca pare em cima da faixa de pedestres.", "🚥 Use seta para indicar suas manobras.",
    "👀 Mantenha os olhos atentos ao trânsito.", "🗺️ Planeje sua rota antes de sair.",
    "🚦 Dê preferência à vida, não ao tempo.", "🎧 Evite usar fones de ouvido ao dirigir.",
    "📵 Nada de redes sociais ao volante.", "🏁 Respeite os limites da via.",
    "🕯️ Ligue o pisca-alerta apenas quando necessário.", "💤 Evite dirigir com sono.",
    "🚷 Não bloqueie cruzamentos.", "📐 Regule os retrovisores corretamente.",
    "🔋 Verifique a bateria antes de viajar.", "🧊 Cuidado com pistas molhadas ou escorregadias.",
    "🔦 Verifique as luzes do veículo.", "🏍️ Use capacete ao pilotar motos.",
    "🚳 Bicicleta também tem regras no trânsito.", "🆘 Saiba acionar socorro em emergências.",
    "🔄 Use a faixa da esquerda só para ultrapassagens.", "🚛 Cuidado com pontos cegos de veículos grandes.",
    "🗣️ Avise manobras com antecedência.", "🚯 Não jogue lixo nas estradas.",
    "🎯 Foco total no volante.", "🚦 Trânsito seguro depende de todos.",
    "✅ Faça sua parte pela segurança no trânsito.", "📢 Compartilhe boas práticas no trânsito."
]

# ==============================================================================
# 3. DEFINIÇÕES DE FUNÇÕES AUXILIARES
# ==============================================================================

def traduz_endereco(endereco_original: str) -> str:
    endereco_traduzido = endereco_original
    for termo_completo, sigla in estado_para_sigla.items():
        if termo_completo in endereco_traduzido:
            endereco_traduzido = endereco_traduzido.replace(termo_completo, sigla)
    return endereco_traduzido.replace(", Brazil", ", Brasil")

def traduz_duracao(texto_duracao: str) -> str:
    texto = texto_duracao.lower()
    texto = texto.replace('days', 'dias').replace('day', 'dia')
    texto = texto.replace('hours', 'horas').replace('hour', 'hora')
    texto = texto.replace('mins', 'minutos').replace('min', 'minuto')
    texto = texto.replace('secs', 'segundos').replace('sec', 'segundo')
    texto = texto.replace(' and ', ' e ')
    return texto

def extract_locations(text: str) -> tuple[str | None, str | None]:
    text_lower = text.lower()
    origem_str = None
    destino_str = None
    match_para = re.search(r'(.+?)\s+para\s+(.+)', text_lower)
    if match_para:
        origem_str = match_para.group(1).strip()
        destino_str = match_para.group(2).strip()
    if origem_str:
        origem_str = quote(origem_str + ", Brasil")
    if destino_str:
        destino_str = quote(destino_str + ", Brasil")
    return origem_str, destino_str

def get_traffic_status(duracao_tipica_segundos: int, duracao_atual_segundos: int) -> tuple[str, str]:
    diferenca = duracao_atual_segundos - duracao_tipica_segundos
    if diferenca <= 0:
        return "🟢 Trânsito fluindo bem.", "Tempo atual melhor ou igual ao típico."
    elif diferenca <= 300:
        return "🟢 Trânsito livre.", "Deslocamento rápido, pouco acima do normal."
    elif diferenca <= 900:
        return "🟡 Trânsito moderado.", "Leves retenções no trajeto."
    else:
        return "🔴 Trânsito pesado.", "Retenções significativas. Considere rotas alternativas."

# ==============================================================================
# 4. DEFINIÇÃO DA FUNÇÃO `handle_message`
# ==============================================================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        print("handle_message: Mensagem vazia ou sem texto.") # Log
        return

    text_input = update.message.text
    print(f"handle_message: Texto recebido: '{text_input}'") # Log
    origem_query, destino_query = extract_locations(text_input)

    if not origem_query or not destino_query:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=("⚠️ Por favor, envie a origem e o destino no formato "
                  "'Cidade Origem para Cidade Destino'.\nExemplo: Curitiba para São Paulo")
        )
        return

    print(f"handle_message: Query para API -> Origem: '{origem_query}', Destino: '{destino_query}'") # Log
    try:
        directions_result = gmaps_client.directions( # gmaps_client usa API_KEY_GOOGLE_MAPS_DIRETO
            origin=origem_query,
            destination=destino_query,
            mode="driving",
            departure_time="now",
            traffic_model="best_guess",
            region="br",
            language="pt-BR",
            alternatives=True
        )
        print("handle_message: Resposta da API Google Maps recebida.") # Log

        if directions_result and len(directions_result) > 0:
            main_route = directions_result[0]
            main_leg = main_route['legs'][0]
            distancia_texto = main_leg['distance']['text']
            duracao_tipica_valor = main_leg['duration']['value']
            duracao_tipica_texto = traduz_duracao(main_leg['duration']['text'])

            if 'duration_in_traffic' in main_leg:
                duracao_atual_com_trafego_valor = main_leg['duration_in_traffic']['value']
                duracao_atual_com_trafego_texto = traduz_duracao(main_leg['duration_in_traffic']['text'])
            else:
                duracao_atual_com_trafego_valor = duracao_tipica_valor
                duracao_atual_com_trafego_texto = duracao_tipica_texto
            
            status_trafego, detalhes_trafego = get_traffic_status(duracao_tipica_valor, duracao_atual_com_trafego_valor)
            rodovias_encontradas_texto = main_route.get('summary', '')
            if rodovias_encontradas_texto:
                 rodovias_encontradas_texto = f"\n🛣️ Via principal: {rodovias_encontradas_texto}"
            
            pedagio_info = ""
            if 'warnings' in main_route and main_route['warnings']:
                for warning in main_route['warnings']:
                    if 'pedágio' in warning.lower() or 'toll' in warning.lower():
                        pedagio_info = "\n💰⚠️ Este trajeto PODE incluir pedágios."
                        break
            
            origem_formatada_api = main_leg['start_address']
            destino_formatado_api = main_leg['end_address']
            maps_link = f"https://www.google.com/maps/dir/?api=1&origin={quote(origem_formatada_api)}&destination={quote(destino_formatado_api)}&travelmode=driving"
            brasilia_tz = pytz.timezone('America/Sao_Paulo')
            current_time_str = datetime.now(brasilia_tz).strftime('%H:%M - %d/%m/%Y')
            origem_br = traduz_endereco(origem_formatada_api)
            destino_br = traduz_endereco(destino_formatado_api)
            mensagem_seguranca_aleatoria = random.choice(mensagens_seguranca)

            message_parts = [
                f"🚦 *ATUALIZAÇÃO DE TRÂNSITO* 🚦\n_{current_time_str}_",
                f"\n➡️ *Origem:* {origem_br}", f"🏁 *Destino:* {destino_br}",
                f"\n📏 *Distância:* {distancia_texto}",
                f"⏳ *Tempo Estimado (com trânsito):* {duracao_atual_com_trafego_texto}",
                f" معمولی *Tempo Típico (sem trânsito pesado):* {duracao_tipica_texto}",
                f"\n{status_trafego} {detalhes_trafego}",
                f"{rodovias_encontradas_texto}{pedagio_info}",
                f"\n🗺️ [Abrir no Google Maps]({maps_link})",
                f"\n\n{mensagem_seguranca_aleatoria}", "\n\n_Fonte: Google Maps API_"
            ]

            if len(directions_result) > 1:
                message_parts.append("\n\n🚗 *Rotas Alternativas Sugeridas:*")
                for i, alt_route in enumerate(directions_result[1:3], 1): # Pega até 2 alternativas
                    alt_leg = alt_route['legs'][0]
                    alt_distancia = alt_leg['distance']['text']
                    alt_duracao_texto = traduz_duracao(alt_leg.get('duration_in_traffic', alt_leg['duration'])['text'])
                    alt_summary = alt_route.get('summary', f'Alternativa {i}')
                    message_parts.append(f"  ➡️ Rota {i} ({alt_summary}): {alt_distancia} - {alt_duracao_texto}")
            
            final_message = "\n".join(filter(None, message_parts))
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=final_message,
                parse_mode=telegram_constants.ParseMode.MARKDOWN
            )
        else: # Se directions_result estiver vazio ou não tiver rotas
            status_api = "N/A"
            if directions_result and isinstance(directions_result, dict) and 'status' in directions_result:
                status_api = directions_result['status']
            elif not directions_result:
                 status_api = "ZERO_RESULTS"
            
            print(f"handle_message: Nenhuma rota encontrada pela API. Status: {status_api}") # Log
            if status_api == "ZERO_RESULTS":
                 await context.bot.send_message(chat_id=update.effective_chat.id, text="😔 Não foram encontradas rotas para os locais informados. Verifique os nomes e tente novamente.")
            else:
                 await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⚠️ Não foi possível obter a rota (Status API: {status_api}). Tente mais tarde.")

    except requests.exceptions.HTTPError as http_err:
        error_content = "Resposta não disponível"
        if hasattr(http_err, 'response') and http_err.response is not None: error_content = http_err.response.text
        print(f"Erro HTTP da API Google Maps: {http_err}, Conteúdo: {error_content}") # Log
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Falha ao comunicar com o serviço de mapas (erro HTTP). Verifique a chave da API e cotas.')
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de conexão com a API do Google Maps: {req_err}") # Log
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Falha ao conectar com o serviço de mapas. Verifique sua conexão.')
    except Exception as e:
        print(f"Erro inesperado em handle_message: {e}") # Log
        import traceback
        traceback.print_exc() # Log detalhado
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Ops! Algo deu muito errado ao processar sua mensagem.')

# ==============================================================================
# 5. BLOCO PRINCIPAL `if __name__ == '__main__':`
# ==============================================================================
if __name__ == '__main__':
    print("Iniciando o bot (usando tokens/chaves embutidas diretamente no código)...")

    if not TOKEN_TELEGRAM_DIRETO: # Checagem final, embora já feita antes
        print("ERRO CRÍTICO FINAL: O token do Telegram (direto) não está definido adequadamente no código.")
        exit()
    if not API_KEY_GOOGLE_MAPS_DIRETO: # Checagem final
        print("ERRO CRÍTICO FINAL: A chave da API do Google Maps (direta) não está definida adequadamente no código.")
        exit()

    try:
        application = ApplicationBuilder().token(TOKEN_TELEGRAM_DIRETO).build()
        message_handler = MessageHandler(
            telegram_filters.TEXT & (~telegram_filters.COMMAND),
            handle_message
        )
        application.add_handler(message_handler)
        print("Bot conectado e escutando por mensagens...")
        application.run_polling()
        print("Bot foi parado.")

    except telegram.error.InvalidToken: # Especificamente para o erro de token do Telegram
        print("ERRO FATAL: O token do Telegram fornecido (diretamente no código) é INVÁLIDO.")
        print("Por favor, gere um novo token no BotFather e atualize a variável TOKEN_TELEGRAM_DIRETO no código.")
    except Exception as e:
        print(f"Erro fatal durante a inicialização ou execução do bot: {e}")
        import traceback
        traceback.print_exc()