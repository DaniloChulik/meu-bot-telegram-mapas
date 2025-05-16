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

from telegram import Update, constants as telegram_constants
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters as telegram_filters
import googlemaps

# ==============================================================================
# 2. CONFIGURAÇÕES DE API E VARIÁVEIS GLOBAIS - COM TOKENS/CHAVES DIRETOS
# ==============================================================================

# !!!!!!!!!! COLOQUE SEUS TOKENS/CHAVES REAIS E VÁLIDOS AQUI !!!!!!!!!!
# Use o token do Telegram que funcionou no check_token.py
TOKEN_TELEGRAM_DIRETO = "7656877931:AAGM80OnUerfpIFfGCEEMjajYvNTtneuBrQ" # <--- SEU TOKEN TELEGRAM VÁLIDO
# Use a chave do Google Maps que funcionou no check_gmaps_key.py
API_KEY_GOOGLE_MAPS_DIRETO = "AIzaSyDoDuV1dpZW41apIdTMYFsXr5ZZS4X2hsU" # <--- SUA CHAVE GOOGLE MAPS VÁLIDA
# !!!!!!!!!! CERTIFIQUE-SE DE QUE ESTES SÃO OS VALORES CORRETOS E SEGUROS !!!!!!!!!!


# Verificações para os tokens/chaves diretas
# Sai se os placeholders não foram substituídos
if not TOKEN_TELEGRAM_DIRETO or "PLACEHOLDER" in TOKEN_TELEGRAM_DIRETO.upper(): # Verifica se contém placeholder
    print("ERRO CRÍTICO: TOKEN_TELEGRAM_DIRETO não foi substituído por um valor real no código.")
    exit()

if not API_KEY_GOOGLE_MAPS_DIRETO or "PLACEHOLDER" in API_KEY_Você está quase lá! O código que você colou é uma mistura da versão que usa variáveis de ambiente (`os.environ.get`) e da versão que usa tokens/chaves embutidas (`TOKEN_TELEGRAM_DIRETO`, `API_KEY_GOOGLE_MAPS_DIRETO`).

**Precisamos escolher UMA abordagem para este arquivo.** Como o objetivo é fazer funcionar primeiro, e você mencionou querer que eu arrume, vamos usar a abordagem com **chaves/tokens embutidos diretamente**, pois ela elimina a complexidade das variáveis de ambiente porGOOGLE_MAPS_DIRETO.upper(): # Verifica se contém placeholder
    print("ERRO CRÍTICO: API_KEY_GOOGLE_MAPS_DIRETO não foi substituído por um valor real no código.")
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
    "🚗 Use sempre o cinto de segurança.", # OK
    "🚧 Mantenha distância segura do veículo à frente.", # OK (se for essa a frase completa)
    "📵 Celular e direção não combinam.", # OK
    # ... continue verificando todas as outras ...
]

```python
# ==============================================================================
# 1. BLOCO DE IMPORTAÇÕES
# ==============================================================================
import json
import requests
import pytz
import random
import re
import os # Pode ser útil para outras coisas no futuro
from datetime import datetime
from urllib.parse import quote

from telegram import Update, constants as telegram_constants
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters as telegram_filters
import googlemaps

# ==============================================================================
# 2. CONFIGURAÇÕES DE API E VARIÁVEIS GLOBAIS - COM TOKENS/CHAVES DIRETOS
# ==============================================================================

# !!!!!!!!!! COLOQUE SEUS TOKENS/CHAVES REAIS E VÁLIDOS AQUI !!!!!!!!!!
# Use o token do Telegram que funcionou no check_token.py
TOKEN_TELEGRAM_DIRETO = "7656877931:AAGM80OnUerfpIFfGCEEMjajYvNTtneuBrQ" # <--- SEU TOKEN TELEGRAM VÁLIDO
# Use a chave do Google Maps que funcionou no check_gmaps_key.py
API_KEY_GOOGLE_MAPS_DIRETO = "AIzaSyDoDuV1dpZW41apIdTMYFsXr5ZZS4X2hsU" # <--- SUA CHAVE GOOGLE MAPS VÁLIDA
# !!!!!!!!!! CERTIFIQUE-SE DE QUE ESTES SÃO OS VALORES CORRETOS E SEGUROS !!!!!!!!!!

# Verificações para os tokens/chaves diretas
# Sai se os placeholders não foram substituídos (ajuste os placeholders se os seus forem diferentes no seu código original)
if not TOKEN_TELEGRAM_DIRETO or TOKEN_TELEGRAM_DIRETO == "SEU_TOKEN_PLACEHOLDER_AQUI.",
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
# =" or len(TOKEN_TELEGRAM_DIRETO) < 40:
    print("ERRO CRÍTICO: TOKEN_TELEGRAM_DIRETO não foi substituído por um valor real e válido no código.")
    exit()

if not API_KEY_GOOGLE_MAPS_DIRETO or API_KEY_GOOGLE_MAPS_DIRETO == "SUA_CHAVE_PLACEHOLDER_AQUI" or len(API_KEY_GOOGLE_MAPS_DIRETO) < 30:
    print("ERRO CRÍTICO: API_KEY_GOOGLE_MAPS_DIRETO não foi substituído por um valor real e válido no código.")
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
    "🕒 Respeite o tempo=============================================================================

def traduz_endereco(endereco_original: str) -> str:
    endereco_traduzido = endereco_original
    for termo_completo, sigla in estado_para_sigla.items():
        if termo_completo in endereco_traduzido:
            endereco_traduzido = endereco_traduzido.replace(termo_completo, sigla)
    return endereco_traduzido.replace(", Brazil", ", Brasil")

def traduz_duracao(texto_duracao: str) -> str:
    """Traduz termos de duração para português e corrige 'minutoutos'."""
    texto = texto_duracao.lower()
    texto = texto.replace('days', 'dias').replace('day', 'dia')
    texto = texto.replace('hours', 'horas').replace('hour', 'hora')
    # Correção para a ordem e para o erro de digitação
    if 'mins' in texto: # Prioriza 'mins' se existir
        texto = texto.replace('mins', 'minutos')
    elif 'min' in texto: # Depois 'min'
        texto = texto.replace('min', 'minuto')
    # Caso a API retorne 'minutes' ou 'minute'
    if 'minutes' in texto:
        texto = texto.replace('minutes', 'minutos')
    elif 'minute' in texto: # Já coberto pelo 'min' acima, mas redundância não faz mal
        texto = texto.replace('minute', 'minuto')

    texto = texto.replace('secs', 'segundos').replace('sec', 'segundo')
    texto = texto.replace(' and ', ' e ')
    return texto

def extract_locations(text: str) -> tuple[str | None, str | None]:
    text_lower = text.lower()
    origem_str = None
    destino_str = None
    # Procura pelo padrão "origem para destino" de forma mais flexível
    match_para = re.search(r'(.+?)\s+(?:para|até|a)\s+(.+)', text_lower, re.IGNORECASE)
    if match_para:
        origem_str = match_para.group(1).strip()
        # Remove frases comuns antes do destino, se existirem
        destino_bruto = match_para.group(2).strip()
        # Tenta limpar um pouco o destino, removendo frases comuns no final
        # ex: "curitiba como está o tempo", pegaria só "curitiba"
        padroes_fim_frase = [r de descanso na direção.", "🍺 Se beber, não dirija.",
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
    # CORREÇÃO para'\scomo está.*', r'\scomo está o trânsito.*', r'\scomo fica.*']
        for padrao in padroes_fim_frase:
            destino_bruto = re.sub(padrao, '', destino_bruto, flags=re.IGNORECASE).strip()
        destino_str = destino_bruto

    if origem_str:
        origem_str = quote(origem_str + ", Brasil")
    if destino_str:
        destino_str = quote(destino_str + ", Brasil")
    return origem_str, destino_str

def get_traffic_status(duracao_tipica_segundos: int, duracao_atual_segundos: int) -> tuple[str, str]:
    diferenca = duracao_atual_segundos - duracao_tipica_segundos
    if diferenca <= 0:
        return "🟢 Trânsito fluindo bem.", "Tempo atual melhor ou igual ao tempo típico."
    elif diferenca <= 300: # Até 5 minutos de atraso
        return "🟢 Trânsito livre.", "Deslocamento rápido, pouco acima do tempo normal."
    elif diferenca <= 900: # Até 15 minutos de atraso
        return "🟡 Trânsito moderado.", "Leves retenções no trajeto."
    else: # Mais de 15 minutos de atraso
        return "🔴 Trânsito pesado.", "Retenções significativas. Considere rotas alternativas."

# ==============================================================================
# 4. DEFINIÇÃO DA FUNÇÃO `handle_message`
# ==============================================================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        print("handle_message: Mensagem vazia ou sem texto.")
        return

    text_input = update.message.text
    print(f"handle_message: Texto recebido: '{text_input}'")

    # Filtro inicial para mensagens que provavelmente não são pedidos de rota
    # Procura por "para", "até" ou "a" entre duas partes.
    if not re.search(r'\s(para|até|a)\s', text_input.lower(), re.IGNORECASE):
        print(f"handle_message: Mensagem '{text_input}' ignorada, não parece ser um pedido de rota explícito.")
        return # Ignora silenciosamente

    orig "minutoutos" -> "minutos"
    texto = texto.replace('minutes', 'minutos').replace('minute', 'minuto') # Se a API retornar 'minutes'
    texto = texto.replace('mins', 'minutos').replace('min', 'minuto') # Cobrindo 'mins' e 'min' também
    texto = texto.replace('secs', 'segundos').replace('sec', 'segundo')
    texto = texto.replace(' and ', ' e ')
    return texto

def extract_locations(text: str) -> tuple[str | None, str | None]:
    text_lower = text.lower()
    origem_str = None
    destino_str = None
    # Tenta encontrar o padrão "origem para destino" de forma mais flexível
    # Remove emojis comuns e palavras de saudação antes de procurar
    text_limpo = re.sub(r'[^\w\s,áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ\-]', '', text_lower) # Mantém letras acentuadas e hífen
    text_limpo = re.sub(r'\b(bom dia|boa tarde|boa noite|olá|como está|como esta)\b', '', text_limpo, flags=re.IGNORECASE).strip()
    
    match_para = re.search(r'(.+?)\s+para\s+(.+)', text_limpo) # Usar text_limpo
    if match_para:
        origem_str = match_para.group(1).strip()
        destino_str = match_paraem_query, destino_query = extract_locations(text_input)

    # Se, mesmo após o filtro inicial, a extração falhar, ignora silenciosamente.
    if not origem_query or not destino_query:
        print(f"handle_message: Não foi possível extrair origem/destino de '{text_input}'. Mensagem ignorada.")
        return # Ignora silenciosamente em vez de enviar erro para o chat

    print(f"handle_message: Query para API -> Origem: '{origem_query}', Destino: '{destino_query}'")
    try:
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
        print("handle_message: Resposta da API Google Maps recebida.")

        if directions_result and len(directions_result) > 0:
            main_route = directions_result[0]
            main_leg = main_route['legs'][0]
            distancia_texto = main_leg['distance']['text']
            duracao_tipica_valor = main_leg['duration']['value']
            duracao_tipica_texto = traduz_duracao(main_leg['duration']['text'])

            if 'duration_in_traffic' in main_leg.group(2).strip()
        
        # Remove excessos comuns no final do destino se a extração for muito longa
        if destino_str and len(destino_str.split()) > 5 : # Heurística, ajustar se necessário
            palavras_destino = destino_str.split()
            # Tenta pegar as primeiras 3-4 palavras como destino principal
            destino_str = " ".join(palavras_destino[:4])


    if origem_str:
        # Evita adicionar ", Brasil" se já parecer um endereço completo ou se for muito curto
        if ',' not in origem_str and len(origem_str.split()) < 4 :
            origem_str = quote(origem_str + ", Brasil")
        else:
            origem_str = quote(origem_str)
            
    if destino_str:
        if ',' not in destino_:
                duracao_atual_com_trafego_valor = main_leg['duration_in_traffic']['value']
                duracao_atual_com_trafego_texto = traduz_duracao(main_leg['duration_in_traffic']['text'])
            else:
                duracao_atual_com_trafego_valor = duracao_tipica_valor
                duracao_atual_com_trafego_texto = duracao_tipica_texto
            
            status_trafego, detalhes_trafego = get_traffic_status(duracao_tipica_valor, duracao_atual_com_trafego_valor)
            rodovias_encontradas_texto = main_route.get('summary', '')
            if rodovias_encontradas_texto:
                 rodovias_encontradas_texto = f"\n🛣️ Via principal: {rodovias_encontradas_texto}"
            
            pedagio_info =str and len(destino_str.split()) < 4 :
            destino_str = quote(destino_str + ", Brasil")
        else:
            destino_str = quote(destino_str)
            
    return origem_str, destino_str

def get_traffic_status(duracao_tipica_segundos: int, duracao_atual_segundos: int) -> tuple[str, str]:
    diferenca = duracao_atual_segundos - duracao_tipica_segundos
    if diferenca <= 0: # Trânsito atual melhor ou igual ao típico
        return "🟢 Trânsito fluindo bem.", "Tempo atual melhor ou igual ao tempo típico."
    elif diferenca <= 300:  # Até 5 minutos de atraso
        return "🟢 Trânsito livre.", "Deslocamento rápido, pouco acima do tempo típico."
     ""
            if 'warnings' in main_route and main_route['warnings']:
                for warning in main_route['warnings']:
                    if 'pedágio' in warning.lower() or 'toll' in warning.lower():
                        pedagio_info = "\n💰⚠️ Este trajeto PODE incluir pedágios."
                        break
            
            origem_formatada_api = main_leg['start_address']
            destino_formatado_api = main_leg['end_address']
            maps_link = f"https://www.google.com/maps/dir/?api=1&origin={quote(origem_formatada_api)}&destination={quote(destino_formatado_api)}&travelmode=driving"
            brasilia_tz = pytz.timezone('America/Sao_Paulo')
            current_time_str = datetime.elif diferenca <= 900:  # Até 15 minutos de atraso
        return "🟡 Trânsito moderado.", "Leves retenções no trajeto."
    else:  # Mais de 15 minutos de atraso
        return "🔴 Trânsito pesado.", "Retenções significativas. Considere rotas alternativas."

# ==============================================================================
# 4. DEFINIÇÃO DA FUNÇÃO `handle_message`
# ==============================================================================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        print("handle_message: Mensagem vazia ou sem texto.")
        return

    text_input = update.now(brasilia_tz).strftime('%H:%M - %d/%m/%Y')
            origem_br = traduz_endereco(origem_formatada_api)
            destino_br = traduz_endereco(destino_formatado_api)
            mensagem_seguranca_aleatoria = random.choice(mensagens_seguranca)

            message_parts = [
                f"🚦 *ATUALIZAÇÃO DE TRÂNSITO* 🚦\n_{current_time_str}_",
                f"\n➡️ *Origem:* {origem_br}", f"🏁 *Destino:* {destino_br}",
                f"\message.text
    print(f"handle_message: Texto recebido: '{text_input}'")
    
    # Filtro simples para evitar processar todas as mensagens em um grupo
    # Só tenta extrair localizações se a palavra "para" (indicando rota) estiver presente.
    # E também ignora mensagens muiton📏 *Distância:* {distancia_texto}",
                f"⏳ *Tempo Estimado (com trânsito):* {duracao_atual_com_trafego_texto}",
                f"🕒 *Tempo Típico (referência):* {duracao_tipica_texto}", # Removido "معمولی"
                f"\n{status_trafego} {detalhes_trafego}",
                f"{rod curtas.
    if " para " not in text_input.lower() or len(text_input) < 10:
        print(f"handle_message: Mensagem '{text_input}' ignorada (não parece ser pedido de rota).")
        return # Não envia mensagem de erro para o usuário, apenas ignora

    origem_query, destino_query = extract_locations(text_input)

    # Se, mesmoovias_encontradas_texto}{pedagio_info}",
                f"\n🗺️ [Abrir no Google Maps]({maps_link})",
                f"\n\n{mensagem_seguranca_aleatoria}", "\n\n_Fonte: Google Maps API_"
            ]

            if len(directions_result) > 1:
                message_parts.append("\n\n🚗 *Rotas Alternativas Sugeridas:*")
                for i, alt_route in enumerate(directions_result[1:3],  com o filtro de " para ", a extração falhar, não envia mensagem.
    if not origem_query or not destino_query:
        print(f"handle_message: Não foi possível extrair origem/destino de '{text_input}'. Ignorando.")
        return # Não envia mensagem de erro para o usuário, apenas ignora

1):
                    alt_leg = alt_route['legs'][0]
                    alt_distancia = alt_leg['distance']['text']
                    alt_duracao_texto = traduz_duracao(alt_leg.get('duration_in_traffic', alt_leg['duration'])['text'])
                    alt_summary = alt_route.get('summary', f'Alternativa {i}')
                    message_parts.append(f"      print(f"handle_message: Query para API -> Origem: '{origem_query}', Destino: '{destino_query}'")
    try:
        directions_result = gmaps_client.directions(
            origin=origem_query,
            destination=destino_query,
            mode="driving",
            departure_time="now",
            traffic_model="best_guess",
            region="br",
            language="pt-➡️ Rota {i} ({alt_summary}): {alt_distancia} - {alt_duracao_texto}")
            
            final_message = "\n".join(filter(None, message_parts))
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=final_message,
                parse_mode=telegram_constants.ParseMode.MARKDOWN
            )BR",
            alternatives=True
        )
        print("handle_message: Resposta da API Google Maps recebida.")

        if directions_result and len(directions_result) > 0:
            main_route = directions_result[0]
            main_leg = main_route['legs'][0]
            distancia_texto = main_leg['distance']['text']
            duracao_tipica_valor = main_leg['duration']['value']
            duracao_tipica_texto = traduz_duracao(main_leg['duration']['text'])

            if 'duration_in_traffic' in main_leg:
                duracao
        else:
            status_api = "N/A"
            if directions_result and isinstance(directions_result, dict) and 'status' in directions_result:
                status_api = directions_result['status']
            elif not directions_result: # Lista vazia
                 status_api = "ZERO_RESULTS"
            
_atual_com_trafego_valor = main_leg['duration_in_traffic']['value']
                duracao_atual_com_trafego_texto = traduz_duracao(main_leg['duration_in_traffic']['text'])
            else:
                duracao_atual_com_trafego_valor = duracao_tipica_valor
                duracao_atual_com_trafego_texto = duracao_tipica_texto
            
            status_trafego, detalhes_trafego = get_traffic_status(            print(f"handle_message: Nenhuma rota encontrada pela API do Google. Status: {status_api}")
            # NÃO ENVIA MENSAGEM PARA O CHAT SE ZERO_RESULTS ou outro erro de rota não encontrada
            # Apenas loga no console.
            if status_api == "ZERO_RESULTS":
                print(f"handle_message: Google API retornou ZERO_RESULTS para '{origem_query}' -> '{destino_queryduracao_tipica_valor, duracao_atual_com_trafego_valor)
            rodovias_encontradas_texto = main_route.get('summary', '')
            if rodovias_encontradas_texto:
                 rodovias_encontradas_texto = f"\n🛣️ Via principal: {rodovias_encontradas_texto}"
            
            pedagio_info = ""
            if 'warnings' in main_route and main_route['warnings']:
                for warning in main_route}'.")
            else:
                print(f"handle_message: Google API retornou status '{status_api}' para '{origem_query}' -> '{destino_query}'.")


    except requests.exceptions.HTTPError as http_err:
        error_content = "Resposta não disponível"
        if hasattr(http_err, 'response') and http_err.response is not None: error_content = http_err.response.text
        print['warnings']:
                    if 'pedágio' in warning.lower() or 'toll' in warning.lower():
                        pedagio_info = "\n💰⚠️ Este trajeto PODE incluir pedágios."
                        break
            
            origem_formatada_api = main_leg['start_address']
            destino_formatada_api = main_leg['end_address']
            maps_link = f"https://www.google.com/maps/dir/?api=1&origin={quote(origem_formatada_api)}&destination={(f"Erro HTTP da API Google Maps: {http_err}, Conteúdo: {error_content}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Falha ao comunicar com o serviço de mapas (erro HTTP). Verifique a chave da API e cotas.')
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de conexão com a API do Google Maps: {req_err}")
        await context.bot.send_message(chat_quote(destino_formatado_api)}&travelmode=driving"
            brasilia_tz = pytz.timezone('America/Sao_Paulo')
            current_time_str = datetime.now(brasilia_tz).strftime('%H:%M - %d/%m/%Y')
            origem_br = traduz_endereco(origem_formatada_api)
            destino_br = traduz_endereco(destino_formatado_api)
            mensagem_seguranca_aleatoria = random.choice(mensagens_segid=update.effective_chat.id, text='⚠️ Falha ao conectar com o serviço de mapas. Verifique sua conexão.')
    except Exception as e:
        print(f"Erro inesperado em handle_message: {e}")
        import traceback
        traceback.print_exc()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='⚠️ Ops! Algo deu muito errado ao processar sua mensagem.')

# ==============================================================================
# 5. BLOCO PRINCIPAL `if __uranca)

            message_parts = [
                f"🚦 *ATUALIZAÇÃO DE TRÂNSITO* 🚦\n_{current_time_str}_",
                f"\n➡️ *Origem:* {origem_br}", f"🏁 *Destino:* {destino_br}",
                f"\n📏 *Distância:* {distancia_texto}",
                f"⏳ *Tempo Estimado (com trânsito):* {duracao_atual_com_trafego_texto}",
                # CORREÇÃO da palavra "معمname__ == '__main__':`
# ==============================================================================
if __name__ == '__main__':
    print("Iniciando o bot (usando tokens/chaves embutidas diretamente no código)...")

    if not TOKEN_TELEGRAM_DIRETO:
        print("ERRO CRÍTICO FINAL: O token do Telegram (direto) não foi definido adequadamente no código.")
        exit()
    if not API_KEY_GOOGLE_MAPS_DIRETO:
        print("ERRO CRÍTICO FINAL: A chave da API do Google Maps (direta) não foi definida adequadamente no código.")
        exit()

ولی"
                f"🕒 *Tempo Típico (sem trânsito pesado):* {duracao_tipica_texto}",
                f"\n{status_trafego} {detalhes_trafego}",
                f"{rodovias_encontradas_texto}{pedagio_info}",
                f"\n🗺️ [Abrir no Google Maps]({maps_link})",
                f"\n\n{mensagem_seguranca_aleatoria}", "\n\n_Fonte: Google Maps API_"
            ]

            if len(directions_result) > 1:
                message_parts.append("\n\n🚗 *Rotas Alternativas Sugeridas:*")
                for i, alt_route in enumerate(directions_result[1:3], 1):
                    alt_leg = alt_route['legs'][0]
                    alt_distancia = alt_leg['distance']['text']
                    alt_duracao_texto = traduz_duracao(    try:
        application = ApplicationBuilder().token(TOKEN_TELEGRAM_DIRETO).build()
        message_handler = MessageHandler(
            telegram_filters.TEXT & (~telegram_filters.COMMAND),
            handle_message
        )
        application.add_handler(message_handler)
        print("Bot conectado e escutando por mensagens...")
        application.run_polling(drop_pending_updates=True) # Adicionado para descartar msgs antigas na inicialização
        print("Bot foi parado.")

    except telegram.error.InvalidToken:
        print("ERRO FATAL: O token do Telegram fornecido (diretamente no código) é INVÁLIDO.")
        print("Por favor, gere um novo token no BotFather e atualize a variável TOKEN_TELEGRAM_DIRETO no código.")
    except Exception as e:
        printalt_leg.get('duration_in_traffic', alt_leg['duration'])['text'])
                    alt_summary = alt_route.get('summary', f'Alternativa {i}')
                    message_parts.append(f"  ➡️ Rota {i} ({alt_summary}): {alt_distancia} - {alt_duracao_texto}")
            
            final_message = "\n".join(filter(None, message_parts))
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=final_message,
                parse_mode=telegram_constants.ParseMode.MARKDOWN
            )
        else:
            status_api = "N/A"
            if directions_result and isinstance(directions_result, dict) and 'status' in directions_result:
                status_(f"Erro fatal durante a inicialização ou execução do bot: {e}")
        import traceback
        traceback.print_exc()