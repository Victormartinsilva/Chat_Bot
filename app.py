from flask import Flask, render_template, request, jsonify
from chatbot import gerar_resposta  # Importa a função do chatbot

app = Flask(__name__, static_url_path='/static')

# Permitir embed do Flask dentro do Dash via iframe
@app.after_request

def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    return response
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/responder', methods=['POST'])
def responder():
    dados = request.get_json()
    mensagem = dados['mensagem']
    resposta, _ = gerar_resposta(mensagem)  # Usa o modelo real
    return jsonify({'resposta': resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)