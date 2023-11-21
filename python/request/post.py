import requests

# URL de destino para a requisição POST
url = 'https://www.example.com/api/post_data'

# Dados a serem enviados (pode ser um dicionário, lista, etc.)
data = {'chave1': 'valor1', 'chave2': 'valor2'}

# Faz uma requisição POST com os dados
response = requests.post(url, data=data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Exibe a resposta do servidor
    print(response.text)
else:
    print(f'A requisição POST falhou com o código de status {response.status_code}')
