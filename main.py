Exemplo de código:
from pysentimiento import create_analyzer
from google import genai

# ==========================================
# ESTRUTURA PRINCIPAL - BOT ANTI-TOXICIDADE
# ==========================================

# Banco de dados temporário na memória
# Formato esperado: { usuario_id: {"score": 100, "advertencias": 0} }
banco_usuarios = {}

# ------------------------------------------
# PARTE 1: INFRAESTRUTURA DO DISCORD
# Aluno 3 (Dev 1) vai trabalhar aqui
# ------------------------------------------
def rodar_bot_discord(token):
    """Inicializa o cliente do bot e escuta as mensagens do chat."""
    # TODO: Dev 1 implementará a conexão e o on_message aqui
    pass


# ------------------------------------------
# PARTE 2: PROCESSAMENTO DE LINGUAGEM NATURAL (NLP)
# Aluno 4 (Dev 2) e Aluno 5 (Dev 3) vão trabalhar aqui
# ------------------------------------------
def verificar_toxicidade_direta(texto, lista_negra):
    """
    Recebe uma string (texto) e uma lista de palavras banidas.
    Retorna True se contiver palavras da lista negra, senão False.
    """
    # TODO: Dev 2 fará a limpeza do texto e busca rápida aqui
    pass

def analisar_sentimento_ia(texto):
    Secret_key = 'nao vou mostrar aqui no codigo'
    client = genai.Client(api_key=Secret_key)
    
    #crio os analisadores
    emoção = create_analyzer(task='emotion', lang='pt')
    hate = create_analyzer(task='hate_speech', lang='pt')
    
    def verificar_anger_escondido(txt: str) -> bool:
        prompt = f"""
            ANALISE o texto e analise se ele contem algum tipo de palavrão ou discurso de ódio escondido,
            RESPONDA EXATAMENTE e APENAS com: "SIM" ou "NÃO".
    
            Texto: "{txt}"
        ""
    
        try:
            response = client.models.generate_content(
                model='models/gemini-3.5-flash',  # Incluindo 'models/' no início
                contents=prompt,
            )
            resultado = response.text.strip().upper()
            return "SIM" in resultado
        except Exception as e:
            print(f"Erro na LLM: {e}")
            return False
    
    def verificar_ironia_llm(texto: str) -> bool:
        prompt = f"""
        Analise o texto a seguir e determine se ele é irônico ou sarcástico.
        Responda EXATAMENTE e APENAS com "SIM" ou "NÃO".
    
        Texto: "{texto}"
        ""
        
        try:
            response = client.models.generate_content(
                model='models/gemini-3.5-flash',  # Incluindo 'models/' no início
                contents=prompt,
            )
            resultado = response.text.strip().upper()
            return "SIM" in resultado
        except Exception as e:
            print(f"Erro na LLM: {e}")
            return False

    while True:    
        frase = input('')#uma frase de exemplo

        rsl_emoção = emoção.predict(frase)#aqui ele preve qual emoção é a da frase
        rsl_hate = hate.predict(frase)
    
        hiden_llm = verificar_anger_escondido(frase)
    
        prob_hate = rsl_hate.probas.get('hateful', 0)
        eh_ironico = verificar_ironia_llm(frase)
    
    
        if eh_ironico:
            print("-> Resultado: É ironia! (Detectado por LLM)")
        else:
            print("-> Resultado: NÃO é ironia.")
    
        if hiden_llm:
            print('-> Contem palavrão escondido!!!')
        else:
            print('-> Não contem palavrão escondido')
    
        print(rsl_emoção.output)
        print(rsl_hate.output)
        
        pass


# ------------------------------------------
# PARTE 3: GAMIFICAÇÃO E DADOS
# Aluno 6 (Dev 4) vai trabalhar aqui
# ------------------------------------------
def atualizar_score_usuario(usuario_id, penalidade):
    """
    Recebe o ID do usuário e o valor a ser subtraído do score dele.
    Atualiza o dicionário 'banco_usuarios'.
    Retorna True se o usuário deve ser MUTADO (score < 50), senão False.
    """
    # TODO: Dev 4 fará a manipulação do dicionário e lógica de punição aqui
    pass
