import logging
import random

# Configura o logging para depuração
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Sistema de respostas inteligentes carregado com sucesso.")

# Limite do histórico para manter o contexto controlado
MAX_CONTEXT_LENGTH = 1000

def limpar_contexto(contexto):
    """Garante que o histórico de contexto não ultrapasse o limite."""
    return contexto[-MAX_CONTEXT_LENGTH:] if len(contexto) > MAX_CONTEXT_LENGTH else contexto

def gerar_resposta(mensagem, contexto=''):
    """Gera uma resposta inteligente baseada em palavras-chave e contexto."""
    
    logging.info(f"Processando mensagem: {mensagem}")
    
    # Usa o sistema inteligente de respostas
    try:
        resposta_final = gerar_resposta_inteligente(mensagem)

        # Atualiza o contexto para a próxima rodada
        novo_contexto = f"{limpar_contexto(contexto)}\nUsuário: {mensagem}\nChimbinha: {resposta_final}\n"

        logging.info(f"Resposta gerada: {resposta_final}")
        return resposta_final, novo_contexto

    except Exception as e:
        logging.error(f"Erro ao gerar resposta: {e}")
        # Fallback para resposta básica
        resposta_fallback = "Desculpe, ocorreu um problema. Tente reformular sua pergunta."
        return resposta_fallback, contexto

def gerar_resposta_inteligente(mensagem):
    """Gera respostas inteligentes baseadas em palavras-chave e contexto."""
    import random
    
    mensagem_lower = mensagem.lower().strip()
    
    # Saudações
    if any(palavra in mensagem_lower for palavra in ['ola', 'oi', 'hello', 'hi', 'bom dia', 'boa tarde', 'boa noite']):
        saudações = [
            "Olá! Como posso ajudá-lo hoje?",
            "Oi! Em que posso ser útil?",
            "Olá! Estou aqui para auxiliar com suas consultas.",
            "Oi! Como posso ajudá-lo com governança de dados?"
        ]
        return random.choice(saudações)
    
    # Perguntas sobre dados
    elif any(palavra in mensagem_lower for palavra in ['dados', 'data', 'informação', 'informacoes', 'banco de dados', 'database', 'formulário', 'formularios', 'formulario', 'gráfico', 'grafico', 'graficos', 'relatório', 'relatorio', 'relatorios', 'tabela', 'tabelas']):
        respostas_dados = [
            "Posso ajudar com questões relacionadas a governança de dados. Qual sua dúvida específica?",
            "Sobre dados: posso auxiliar com políticas, qualidade, segurança ou compliance. O que gostaria de saber?",
            "Governança de dados é minha especialidade. Qual aspecto você gostaria de abordar?",
            "Posso ajudar com classificação, catalogação, linhagem ou qualidade de dados. Qual sua necessidade?",
            "Para formulários e relatórios: posso auxiliar com estrutura, validação, coleta e análise de dados.",
            "Sobre gráficos e visualizações: posso ajudar com boas práticas de apresentação de dados e compliance."
        ]
        return random.choice(respostas_dados)
    
    # Perguntas sobre o sistema
    elif any(palavra in mensagem_lower for palavra in ['como', 'how', 'funciona', 'sistema', 'bot', 'você']):
        respostas_sistema = [
            "Sou o Chimbinha Bot, especializado em governança de dados. Posso ajudar com políticas, qualidade e compliance.",
            "Funciono como assistente para questões de dados. Faça perguntas sobre governança, qualidade ou segurança.",
            "Sou um chatbot profissional para auxiliar em temas de governança de dados. Como posso ajudar?",
            "Meu objetivo é facilitar o trabalho com dados organizacionais. Qual sua necessidade?"
        ]
        return random.choice(respostas_sistema)
    
    # Perguntas sobre qualidade
    elif any(palavra in mensagem_lower for palavra in ['qualidade', 'quality', 'duplicado', 'inconsistente', 'limpeza']):
        respostas_qualidade = [
            "Para qualidade de dados, recomendo: validação na entrada, regras de negócio claras e monitoramento contínuo.",
            "Qualidade de dados envolve precisão, completude, consistência e atualidade. Qual aspecto específico?",
            "Implemente processos de validação, limpeza e padronização para garantir qualidade dos dados.",
            "Qualidade de dados é fundamental. Posso ajudar com estratégias de melhoria e monitoramento."
        ]
        return random.choice(respostas_qualidade)
    
    # Perguntas sobre segurança
    elif any(palavra in mensagem_lower for palavra in ['segurança', 'seguranca', 'security', 'privacy', 'privacidade', 'lgpd', 'gdpr']):
        respostas_seguranca = [
            "Segurança de dados envolve controle de acesso, criptografia, auditoria e compliance. Qual seu foco?",
            "Para LGPD/GDPR, é essencial: mapeamento de dados, consentimento, direito ao esquecimento e proteção.",
            "Segurança em dados requer classificação, controle de acesso e monitoramento de atividades.",
            "Posso ajudar com políticas de segurança, classificação de dados e compliance regulatório."
        ]
        return random.choice(respostas_seguranca)
    
    # Perguntas sobre políticas
    elif any(palavra in mensagem_lower for palavra in ['política', 'politica', 'policy', 'governança', 'governanca', 'framework']):
        respostas_politicas = [
            "Políticas de governança devem cobrir: classificação, acesso, qualidade, segurança e lifecycle dos dados.",
            "Um framework de governança inclui: estrutura organizacional, processos, tecnologias e métricas.",
            "Políticas eficazes definem responsabilidades, procedimentos e controles para gestão de dados.",
            "Governança de dados requer políticas claras sobre propriedade, qualidade e uso dos dados."
        ]
        return random.choice(respostas_politicas)
    
    # Perguntas sobre compliance
    elif any(palavra in mensagem_lower for palavra in ['compliance', 'auditoria', 'auditoria', 'regulamentação', 'regulamentacao']):
        respostas_compliance = [
            "Compliance requer documentação, controles internos, auditorias regulares e treinamento da equipe.",
            "Para compliance, implemente controles de acesso, logs de auditoria e políticas documentadas.",
            "Auditoria de dados deve verificar: integridade, segurança, qualidade e conformidade regulatória.",
            "Compliance envolve monitoramento contínuo, relatórios e correção de não-conformidades."
        ]
        return random.choice(respostas_compliance)
    
    # Despedidas
    elif any(palavra in mensagem_lower for palavra in ['tchau', 'bye', 'até logo', 'obrigado', 'obrigada', 'valeu']):
        despedidas = [
            "De nada! Estou sempre disponível para ajudar com governança de dados.",
            "Foi um prazer ajudar! Volte sempre que precisar.",
            "Por nada! Qualquer dúvida sobre dados, estou aqui.",
            "Disponha! Estou sempre pronto para auxiliar."
        ]
        return random.choice(despedidas)
    
    # Perguntas sobre ajuda
    elif any(palavra in mensagem_lower for palavra in ['ajuda', 'help', 'dúvida', 'duvida', 'não sei', 'nao sei']):
        respostas_ajuda = [
            "Posso ajudar com governança de dados, qualidade, segurança, compliance e políticas. Qual sua necessidade?",
            "Sou especialista em governança de dados. Faça perguntas sobre políticas, qualidade ou segurança.",
            "Posso auxiliar em temas como: classificação de dados, controle de acesso, qualidade e compliance.",
            "Estou aqui para ajudar com governança de dados. Seja específico na sua pergunta para melhor atendimento."
        ]
        return random.choice(respostas_ajuda)
    
    # Resposta padrão para mensagens não reconhecidas
    else:
        respostas_padrao = [
            "Interessante pergunta! Posso ajudar melhor se você for mais específico sobre governança de dados.",
            "Entendi sua mensagem. Para melhor atendimento, seja mais específico sobre sua necessidade.",
            "Posso ajudar com governança de dados, qualidade, segurança ou compliance. Qual sua dúvida?",
            "Faça perguntas mais específicas sobre dados para que eu possa ajudá-lo melhor.",
            "Sou especialista em governança de dados. Como posso ser mais útil para você?"
        ]
        return random.choice(respostas_padrao)

def gerar_resposta_fallback(mensagem):
    """Fallback para casos de erro - usa o sistema inteligente."""
    return gerar_resposta_inteligente(mensagem)

# Execução local para testes no terminal
if __name__ == "__main__":
    contexto = ""
    print("Chimbinha Bot ativo! Digite sua mensagem. (digite 'sair' para encerrar)")
    while True:
        user_msg = input("Você: ")
        if user_msg.lower().strip() in ["sair", "exit", "fim"]:
            print("Chimbinha: Encerrando sessão. Até logo!")
            break
        resposta, contexto = gerar_resposta(user_msg, contexto)
        print(f"Chimbinha: {resposta}")