import requests

# URL da página que você deseja acessar
url = 'https://www.mullertec.com.br'

# Faz uma requisição GET à URL
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Exibe o conteúdo da página
    print(response.text)
else:
    print(f'A requisição falhou com o código de status {response.status_code}')
