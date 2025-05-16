# ==============================================================================
# 1. BLOCO DE IMPORTAÇÕES
# ==============================================================================
import json
import requests
import pytz
import random
import re
import os # Mantido caso seja usado para algo mais no futuro
from datetime import datetime
from urllib.parse import quote
import traceback # Usado no tratamento de exceções

from telegram import Update, constants as telegram_constants
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters as telegram_filters, CommandHandler
import googlemaps

# ==============================================================================
# 2. CONFIGURAÇÕES DE API E VARIÁVEIS GLOBAIS - COM TOKENS/CHAVES DIRETOS
# ==============================================================================

# !!!!!!!!!! CERTIFIQUE-SE DE QUE ESTAS SÃO SUAS CHAVES VÁLIDAS !!!!!!!!!!
# Use o token do Telegram que funcionou no check_token.py
TOKEN_TELEGRAM_DIRETO = "7656877931:AAGM80OnUerfpIFfGCEEMjajYvNTtneuBrQ"
# Use a chave do Google Maps que funcionou no check_gmaps_key.py
API_KEY_GOOGLE_MAPS_DIRETO = "AIzaSyDoDuV1dpZW41apIdTMYFsXr5ZZS4X2hsU"
# !!!!!!!!!! FIM DA SEÇÃO DE CHAVES !!!!!!!!!!


# Verificações para garantir que as chaves foram definidas com algum valor
if not TOKEN_TELEGRAM_DIRETO or len(TOKEN_TELEGRAM_DIRETO) < 40 :
    print("ERRO CRÍTICO: TOKEN_TELEGRAM_DIRETO parece inválido ou não definido no código.")
    exit()

if not API_KEY_GOOGLE_MAPS_DIRETO or len(API_KEY_GOOGLE_MAPS_DIRETO) < 30:
     print("ERRO CRÍTICO: API_KEY_GOOGLE_MAPS_DIRETO parece inválido ou não definido no código.")
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
    """Traduz termos de duração para português."""
    texto = texto_duracao.lower()
    texto = texto.replace('days', 'dias').replace('day', 'dia')
    texto = texto.replace('hours', 'horas').replace('hour', 'hora')
    # Lógica de substituição corrigida para minutos:
    if 'minutes' in texto:
        texto = texto.replace('minutes', 'minutos')
    elif 'minute' in texto:
         texto = texto.replace('minute', 'minuto')
    elif 'mins' in texto: # Fallback para 'mins'
        texto = texto.replace('mins', 'minutos')
    elif 'min' in texto: # Fallback para 'min'
         texto = texto.replace('min', 'minuto')

    texto = texto.replace('secs', 'segundos').replace('sec', 'segundo')
    texto = texto.replace(' and ', ' e ')
    return texto

def extract_locations(text: str) -> tuple[str | None, str | None]:
    """ Tenta extrair 'Origem para Destino' do texto."""
    text_lower = text.lower()
    origem_str = None
    destino_str = None
    # Procura pelo padrão "origem para destino"
    match_para = re.search(r'(.+?)\s+para\s+(.+)', text_lower, re.IGNORECASE)
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
        return "🟢 Trânsito fluindo bem.", "Tempo atual melhor ou igual ao tempo típico."
    elif diferenca <= 300:
        return "🟢 Trânsito livre.", "Deslocamento rápido, pouco acima do normal."
    elif diferenca <= 900:
        return "🟡 Trânsito moderado.", "Leves retenções no trajeto."
    else:
        return "🔴 Trânsito pesado.", "Retenções significativas. Considere rotas alternativas."

# ==============================================================================
# 4. DEFINIÇÃO DA FUNÇÃO `handle_message` (HANDLER PRINCIPAL)
# ==============================================================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagens de texto, IGNORANDO silenciosamente as que não parecerem pedidos de rota."""
    if update.message is None or update.message.text is None:
        return # Ignora mensagens sem texto

    text_input = update.message.text
    
    # >>> AJUSTE 1: Filtro inicial para ignorar mensagens que não contêm " para " <<<
    # Se não tiver " para " (ignorando maiúsculas/minúsculas), sai da função sem responder.
    if " para " not in text_input.lower():
        print(f"INFO: Mensagem ignorada (não contém ' para '): '{text_input[:80]}...'")
        return # Ignora silenciosamente

    print(f"INFO: Processando texto recebido: '{text_input}'")
    origem_query, destino_query = extract_locations(text_input)

    # >>> AJUSTE 2: Se a extração falhar (mesmo tendo " para "), também ignora silenciosamente <<<
    if not origem_query or not destino_query:
        print(f"INFO: Não foi possível extrair Origem/Destino válidos de '{text_input}'. Ignorando.")
        return # Ignora silenciosamente

    print(f"INFO: Query para API -> Origem: '{origem_query}', Destino: '{destino_query}'")
    try:
        # Chamada para a API do Google
        directions_result = gmaps_client.directions(
            origin=origem_query,
            destination=destino_query,
            mode="driving",
            departure_time="now",
            traffic_model="best_guess",
            region="br",
            language="pt-BR",
            alternatives=True
        )
        print("INFO: Resposta da API Google Maps recebida.")

        # Processa se houver rotas
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

            # Monta a mensagem de resposta
            message_parts = [
                f"🚦 *ATUALIZAÇÃO DE TRÂNSITO* 🚦\n_{current_time_str}_",
                f"\n➡️ *Origem:* {origem_br}", f"🏁 *Destino:* {destino_br}",
                f"\n📏 *Distância:* {distancia_texto}",
                f"⏳ *Tempo Estimado (com trânsito):* {duracao_atual_com_trafego_texto}",
                f"🕒 *Tempo Típico (referência):* {duracao_tipica_texto}", # <<< CORRIGIDO: Removida palavra estranha
                f"\n{status_trafego} {detalhes_trafego}",
                f"{rodovias_encontradas_texto}{pedagio_info}",
                f"\n🗺️ [Abrir no Google Maps]({maps_link})",
                f"\n\n{mensagem_seguranca_aleatoria}",
                 "\n\n_Fonte: Google Maps API_"
            ]

            # Adiciona rotas alternativas, se houver
            if len(directions_result) > 1:
                message_parts.append("\n\n🚗 *Rotas Alternativas Sugeridas:*")
                for i, alt_route in enumerate(directions_result[1:3], 1): # Pega até 2
                    alt_leg = alt_route['legs'][0]
                    alt_distancia = alt_leg['distance']['text']
                    alt_duracao_texto = traduz_duracao(alt_leg.get('duration_in_traffic', alt_leg['duration'])['text'])
                    alt_summary = alt_route.get('summary', f'Alternativa {i}')
                    message_parts.append(f"  ➡️ Rota {i} ({alt_summary}): {alt_distancia} - {alt_duracao_texto}")
            
            final_message = "\n".join(filter(None, message_parts))
            
            # Envia a resposta
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=final_message,
                parse_mode=telegram_constants.ParseMode.MARKDOWN
            )
        
        else:
             # >>> AJUSTE 3: Se a API do Google não retornar rotas, APENAS LOGA, NÃO ENVIA MENSAGEM <<<
            status_api = "UNKNOWN"
            if directions_result and isinstance(directions_result, dict) and 'status' in directions_result:
                 status_api = directions_result['status']
            elif not directions_result:
                 status_api = "ZERO_RESULTS"
            print(f"INFO: Nenhuma rota encontrada pela API do Google. Status: {status_api}. Mensagem NÃO enviada para o chat.")

    except requests.exceptions.HTTPError as http_err:
        # Erros da API do Google (chave inválida, cota excedida, etc)
        error_content = "Resposta não disponível"
        if hasattr(http_err, 'response') and http_err.response is not None: error_content = http_err.response.text
        print(f"ERRO: Erro HTTP da API Google Maps: {http_err}, Conteúdo: {error_content}")
        # Opcional: Enviar uma mensagem de erro para o chat, se quiser.
        # await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Falha interna ao buscar dados de mapa. Tente mais tarde.')
    except (requests.exceptions.RequestException, telegram.error.TimedOut) as req_err:
         # Erros de Rede (conexão, timeout do Telegram)
        print(f"ERRO: Erro de Rede/Timeout: {req_err}")
        # Não envia mensagem para o usuário, pois pode ser um problema temporário de rede
    except telegram.error.RetryAfter as flood_err:
         print(f"ERRO: Flood control do Telegram excedido: {flood_err}")
         # Não envia mensagem para o usuário
    except Exception as e:
        # Outros erros inesperados no código
        print(f"ERRO: Erro inesperado em handle_message: {e}")
        traceback.print_exc()
        # Opcional: Enviar uma mensagem genérica de erro
        # await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Ops! Ocorreu um erro interno.')


# ==============================================================================
# 5. BLOCO PRINCIPAL `if __name__ == '__main__':`
# ==============================================================================
async def post_init(application: ApplicationBuilder) -> None:
     """ Descarta updates pendentes ao iniciar."""
     await application.bot.get_updates(offset=-1, timeout=1)
     print("INFO: Updates pendentes descartados.")
     
if __name__ == '__main__':
    print("Iniciando o bot (usando tokens/chaves embutidas diretamente no código)...")

    if not TOKEN_TELEGRAM_DIRETO:
        print("ERRO CRÍTICO FINAL: O token do Telegram (direto) não foi definido adequadamente no código.")
        exit()
    if not API_KEY_GOOGLE_MAPS_DIRETO:
        print("ERRO CRÍTICO FINAL: A chave da API do Google Maps (direta) não foi definida adequadamente no código.")
        exit()

    try:
        # Adicionando um handler para o comando /start e /ajuda
        async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
            ajuda_texto = (
                "Olá! Sou seu bot de rotas e trânsito.\n\n"
                "Para consultar, envie uma mensagem no formato:\n"
                "`Local de Origem para Local de Destino`\n\n"
                "Exemplo: `Curitiba para São Paulo`"
             )
            await update.message.reply_text(ajuda_texto, parse_mode=telegram_constants.ParseMode.MARKDOWN)

        application = ApplicationBuilder().token(TOKEN_TELEGRAM_DIRETO).build()
        
        # application.post_init = post_init # Habilitar esta linha pode ajudar a descartar updates antigos, mas use com cuidado

        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("ajuda", start_command))
        
        message_handler = MessageHandler(
            telegram_filters.TEXT & (~telegram_filters.COMMAND), # Ignora comandos (/start, /ajuda) para este handler
            handle_message
        )
        application.add_handler(message_handler)
        
        print("Bot conectado e escutando por mensagens...")
        # Adicionado drop_pending_updates=True para tentar ajudar com flood na inicialização
        application.run_polling(drop_pending_updates=True) 
        
        print("Bot foi parado.")

    except telegram.error.InvalidToken:
        print("ERRO FATAL: O token do Telegram fornecido (diretamente no código) é INVÁLIDO.")
        print("Por favor, gere um novo token no BotFather e atualize a variável TOKEN_TELEGRAM_DIRETO no código.")
    except Exception as e:
        print(f"Erro fatal durante a inicialização ou execução do bot: {e}")
        traceback.print_exc()