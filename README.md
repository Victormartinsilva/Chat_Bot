# Chimbinha Bot - Chatbot Profissional

Um chatbot inteligente para governança de dados, desenvolvido com Flask e sistema de respostas baseado em palavras-chave, com interface profissional e moderna.

## 🌐 **Demo Online**

**🚀 [Teste o Chatbot Aqui](https://chat-bot-7g95.onrender.com/)**

[![Deploy Status](https://img.shields.io/badge/Deploy-Render-green)](https://chat-bot-7g95.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-red)](https://flask.palletsprojects.com)

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/Chat_Bot.git
   cd Chat_Bot
   ```

2. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o chatbot:**
   ```bash
   python app.py
   ```

4. **Acessar o chatbot:**
   - Abra seu navegador
   - Vá para: `http://localhost:5000`

## 🌐 Deploy no GitHub Pages / Heroku / Railway

### Opção 1: Heroku (Recomendado)

1. **Instale o Heroku CLI** e faça login
2. **Crie um arquivo `Procfile`:**
   ```
   web: python app.py
   ```
3. **Configure as variáveis de ambiente** no Heroku
4. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy para Heroku"
   heroku create seu-chimbinha-bot
   git push heroku main
   ```

### Opção 2: Railway

1. **Conecte seu repositório** no Railway
2. **Configure as variáveis** de ambiente
3. **Deploy automático** a cada push

### Opção 3: Render ✅ **USADO NESTE PROJETO**

1. **Conecte o repositório** no [Render](https://render.com)
2. **Configure o build command:** `pip install -r requirements.txt`
3. **Configure o start command:** `python app.py`
4. **Resultado:** [https://chat-bot-7g95.onrender.com/](https://chat-bot-7g95.onrender.com/)

**✅ Deploy realizado com sucesso no Render!**

## 🎯 Funcionalidades

- Interface web responsiva com design profissional
- Respostas inteligentes baseadas em palavras-chave
- Chat sempre inicia limpo (sem histórico anterior)
- Conversas armazenadas apenas na sessão atual
- Indicador de carregamento durante processamento
- Design corporativo adequado para governança de dados

## 🛠️ Solução de Problemas

### Modelo não carrega
Se o modelo GPT-2 em português não carregar, o sistema automaticamente:
1. Tenta carregar o modelo GPT-2 padrão em inglês
2. Se ambos falharem, usa respostas pré-definidas

### Erro de dependências
Execute novamente:
```bash
pip install -r requirements.txt --upgrade
```

### Chatbot não responde corretamente
Se o chatbot não estiver respondendo com as respostas inteligentes:

1. **Limpe o cache do navegador:**
   - Pressione `Ctrl + Shift + R` (Windows) ou `Cmd + Shift + R` (Mac)
   - Ou pressione `F12` e clique com botão direito no botão de atualizar → "Esvaziar cache e recarregar forçado"

2. **Verifique se o servidor está rodando:**
   ```bash
   python app.py
   ```

3. **Teste a API diretamente:**
   ```bash
   # No PowerShell
   Invoke-WebRequest -Uri "http://localhost:5000/responder" -Method POST -ContentType "application/json" -Body '{"mensagem": "oi"}'
   ```

### Porta ocupada
Se a porta 5000 estiver ocupada, altere no arquivo `app.py`:
```python
app.run(host="0.0.0.0", port=5001, debug=False)  # Mude para 5001 ou outra porta
```

## 📁 Estrutura do Projeto

```
Chat_Bot/
├── app.py              # Aplicação Flask principal
├── chatbot.py          # Lógica do chatbot com GPT-2
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html     # Interface web
├── static/
│   └── chimbinha-avatar.png
└── README.md          # Este arquivo
```

## 📊 Sobre o Chimbinha Bot

O Chimbinha Bot é uma solução profissional de chatbot desenvolvida para ambientes corporativos e governança de dados. Com interface moderna e design limpo, oferece uma experiência de usuário profissional e eficiente para consultas e interações empresariais.

### 🎯 Características Técnicas

- **Framework:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Sistema de Respostas:** Baseado em palavras-chave inteligentes
- **Design:** Interface corporativa responsiva
- **Deploy:** Pronto para Heroku, Railway, Render

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Victor Silva**
- GitHub: [@Victormartinsilva](https://github.com/Victormartinsilva)
- Projeto: [Chat_Bot Repository](https://github.com/Victormartinsilva/Chat_Bot)
- Demo: [https://chat-bot-7g95.onrender.com/](https://chat-bot-7g95.onrender.com/)

