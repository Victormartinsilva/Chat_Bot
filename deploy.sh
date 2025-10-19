#!/bin/bash

# Script de Deploy para GitHub e Heroku
echo "🚀 Iniciando deploy do Chimbinha Bot..."

# Verificar se git está inicializado
if [ ! -d ".git" ]; then
    echo "📦 Inicializando repositório Git..."
    git init
    git add .
    git commit -m "Initial commit: Chimbinha Bot"
    echo "✅ Repositório Git inicializado!"
fi

# Verificar status do git
echo "📊 Status do repositório:"
git status

# Adicionar todos os arquivos
echo "📁 Adicionando arquivos ao Git..."
git add .

# Commit das mudanças
echo "💾 Fazendo commit das mudanças..."
git commit -m "Update: Melhorias no chatbot e preparação para deploy"

echo "✅ Deploy local preparado!"
echo ""
echo "📋 Próximos passos:"
echo "1. Crie um repositório no GitHub"
echo "2. Execute: git remote add origin https://github.com/SEU_USUARIO/Chat_Bot.git"
echo "3. Execute: git push -u origin main"
echo ""
echo "🌐 Para deploy no Heroku:"
echo "1. heroku create seu-chimbinha-bot"
echo "2. git push heroku main"
echo ""
echo "🎯 Para deploy no Railway:"
echo "1. Conecte o repositório no Railway"
echo "2. Deploy automático!"
