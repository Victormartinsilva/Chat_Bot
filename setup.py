#!/usr/bin/env python3
"""
Script de configuração para o Chimbinha Bot
"""

import os
import sys
import subprocess

def install_requirements():
    """Instala as dependências do projeto"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False
    return True

def create_env_file():
    """Cria arquivo .env de exemplo"""
    env_content = """# Configurações do Chimbinha Bot
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
"""
    
    if not os.path.exists('.env'):
        with open('.env', 'w', encoding='utf-8') as f:
            f.write(env_content)
        print("📄 Arquivo .env criado!")
    else:
        print("📄 Arquivo .env já existe!")

def main():
    """Função principal"""
    print("🎸 Configurando Chimbinha Bot...")
    print("=" * 40)
    
    # Instalar dependências
    if not install_requirements():
        print("❌ Falha na configuração!")
        sys.exit(1)
    
    # Criar arquivo .env
    create_env_file()
    
    print("=" * 40)
    print("✅ Configuração concluída!")
    print("\n🚀 Para executar o bot:")
    print("   python app.py")
    print("\n🌐 Acesse: http://localhost:5000")

if __name__ == "__main__":
    main()
