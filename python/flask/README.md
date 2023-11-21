O Flask é um microframework web em Python que é leve e fácil de usar. Ele oferece flexibilidade aos desenvolvedores, permitindo que eles escolham as bibliotecas e ferramentas que desejam usar em seu projeto.

É uma escolha excelente para projetos web que não exigem uma estrutura completa de framework, mas que se beneficiariam de uma abordagem simples e modular para o desenvolvimento web em Python. É uma excelente opção para iniciantes e para quem deseja aprender sobre desenvolvimento web com Python.

Documentação em: https://flask.palletsprojects.com/en/3.0.x/

#### Preparando o ambiente..

Verifique se o Python e o pip estão instalados: 

    python3 --version && pip --version

Certifique-se de que o Python seja uma versão 3.x (por exemplo, Python 3.6, 3.7, 3.8, etc.) e que o pip esteja instalado. Se não estiver, você pode instalar o pip para Python 3 da seguinte maneira:

    sudo apt install python3-pip python3-virtualenv

Criando um ambiente virtual, é uma boa prática criar um ambiente virtual para isolar as dependências do flask de outras aplicações python no sistema:

    python3 -m venv .venv

Ativando o ambiente virtual:

    source .venv/bin/activate

Para sair:

    deactivate

Instalando o flask dentro do ambiente virtual, com seu ambiente virtual ativo (se você optou por criar um), você pode instalar:

    sudo pip install flask

O arquivo requirements.txt possui uma lista de todas as bibliotecas necessárias para o nosso projeto, podemos imprimir na tela seu contee alimentar o arquivo para 

Imprimindo todas as bibliotecas python instaladas no ambiente virtual atual:

    pip freeze

Utilizamos e saída para ir sempre alimentando o arquivo requirements.txt que será utilizado no Dokerfile:

    pip freeze > requirements.txt

Iniciando o projeto:

    flask run