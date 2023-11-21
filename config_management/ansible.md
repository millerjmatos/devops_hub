O Ansible é uma ferramenta de automação de TI de código aberto que simplifica e agiliza o gerenciamento de configurações, provisionamento de servidores e implantação de aplicativos em ambientes heterogêneos. Utilizando uma abordagem baseada em YAML, o Ansible permite que os usuários descrevam as tarefas em linguagem humana, eliminando a necessidade de scripts complexos. Com uma vasta biblioteca de módulos e a capacidade de criar e compartilhar papéis, o Ansible simplifica a implementação de infraestrutura e a configuração de aplicativos, promovendo a padronização e a escalabilidade em projetos de qualquer tamanho.

Instalação no Ubuntu:

    sudo apt update
    
    sudo apt install software-properties-common
    
    sudo add-apt-repository --yes --update ppa:ansible/ansible
    
    sudo apt-get install ansible

Crie os arquivos:

    hosts.yml

Edite:
        [ansible-terraform-aws]
        52.45.96.222

    playbook.yml

Edite:

        - hosts: ansible-terraform-aws
            tasks:
        - name: criando o arquivo
            copy:
                dest: /home/ubuntu/index.html
                content: <h1>Feito com terraform e ansible</h1>
        - name: criando o servidor
            shell: "nohup busybox httpd -f -p 8080 &"

Executando:

    ansible-playbook.yml -u ubuntu --private-key iac-muller.pem -i hosts.yml

Usando python:

        - hosts: ansible-terraform-aws
            tasks:
        - name: Instalando o python3, virtualenv
            apt:
                pkg:
                - python3
                - virtualenv
                update_cache: yes
            become: yes

Executar o playbook e atentar para o hosts.yml.

Instalando dependências:

        - hosts: ansible-terraform-aws
            tasks:
        - name: Instalando o python3, virtualenv
            apt:
                pkg:
                - python3
                - virtualenv
                update_cache: yes
            become: yes
        - name: Instalando dependências com pip (Django e Django Rest)
            pip: 
                virtualenv: /home/ubuntu/project/venv
                name:
                    - django
                    - djangorestframework
            
Executar o playbook e atentar para o hosts.yml.

Acessar a máquina e ativar o virtualenv:

    . /home/ubuntu/project/venv/bin/activate

Verificando os pacotes instalados:

    pip freeze

O Ansible tem uma grande integração com o Python, então ele tem comandos prontos para certas ações, como instalar dependências com o pip e pip3, e criar ambientes virtuais, também conhecidos como “Virtual environments", para instalar as dependências dentro deles, permitindo que a máquina tenha apenas o necessário na hora da execução.

No servidor..

Já instalamos o Django e o Django rest através do Ansible na venv.

    django-admin startproject

    python manage.py runserver 0.0.0.0:8000

Abrindo o projeto:

    vim <caminho_projeto>/settings.py

Edite:

        ALLOWED_HOSTS = ["*"]

        :x

Executando novamente:

    python manage.py runserver 0.0.0.0:8000

Acesso o IP na porta específica em seu navegador.

Utilizando o shell:

    - name: Iniciando o projeto
        shell: 'comando 1; comando 2; comando 3'

ou

    - name: Iniciando o projeto
        shell: 'comando 1'
        shell: 'comando 2'

Alterando o parâmetro ALLOWED_HOSTS = [] para ALLOWED_HOSTS = ["*"]:

    lineinfile:
        path: /home/ubuntu/project/setup/settings.py
        regexp: 'ALLOWED_HOSTS'
        line: 'ALLOWED_HOSTS = ["*"]'
        backrefs: yes

Ignorando erros:

    - name: Iniciando o projeto
        shell: '. /home/ubuntu/project/venv/bin/activate; django-admin startproject setup /home/ubuntu/project/'
        ignore_errors: yes

Quando você define "ignore_errors" como "yes", o Ansible registrará o erro, mas não interromperá a execução do playbook.

Durante a inicialização do projeto, feito através do comando django-admin startproject setup podemos encontrar um erro, e esse erro é sobre substituir arquivos já existentes. No caso do Django, a substituição não é realizada por questões de segurança!