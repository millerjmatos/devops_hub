O PyCharm é um poderoso ambiente de desenvolvimento integrado (IDE) voltado para a linguagem de programação Python. Desenvolvido pela JetBrains, o PyCharm oferece uma ampla gama de recursos e ferramentas para facilitar o processo de codificação, depuração, teste e análise de projetos em Python. Com uma interface intuitiva e amigável, o IDE possui recursos avançados, como sugestões de código inteligentes, refatoração automática, integração com sistemas de controle de versão, suporte a virtualenv, além de facilitar o gerenciamento de dependências e a execução de testes. Esses recursos tornam o PyCharm uma escolha popular entre desenvolvedores Python, permitindo-lhes serem mais produtivos e eficientes no desenvolvimento de seus projetos.

Site para download do PyCharm: https://www.jetbrains.com/pycharm/download/

## Instalação no Linux Mint 20.3:

Extraindo o arquivo:

    tar -xzf nome_do_arquivo.tar.gz

Movendo para /opt para instalação global:

    sudo mv <nome_do_diretorio> pycharm && mv pycharm /opt/

Criando atalho:

    vim ~/.local/share/applications/pycharm.desktop

Cole:

        [Desktop Entry]
        Name=PyCharm
        Comment=Python IDE
        Exec=/opt/pycharm/bin/pycharm.sh
        Icon=/opt/pycharm/bin/pycharm.png
        Terminal=false
        Type=Application
        Categories=Development;IDE;
        StartupNotify=true

Permissão:

    chmod +x /opt/pycharm/bin/pycharm.sh

Executando:

    /opt/pycharm/bin/pycharm.sh