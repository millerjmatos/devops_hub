# Exemplo simples de uma API REST que retorna uma mensagem "Hello, World!"
# quando você acessa o endpoint /hello:

from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
