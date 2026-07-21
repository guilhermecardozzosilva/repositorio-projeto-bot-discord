Exemplo de código:
from pysentimiento import create_analyzer

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
    emoção = create_analyzer(task='emotion', lang='pt')
    ironia = create_analyzer(task='irony', lang='pt')

    rsl_emoção = emoção.predict(texto)
    rsl_ironia = ironia.predict(texto)

    if rsl_ironia.output == 'ironic':
        pass #não faz nada pois é ironia
    elif rsl_ironia.output == 'not ironic' and rsl_emoção.output == 'anger':
        print('discurso de ódio, pode conter palavrão') #ainda tem que ver o que pode fazer aqui
    
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
