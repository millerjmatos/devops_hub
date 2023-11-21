O AWS CLI (Command Line Interface) é uma ferramenta de linha de comando da Amazon Web Services (AWS) que permite interagir com os serviços da AWS através de comandos de texto, facilitando a automação e administração de recursos na nuvem. Ele unifica várias operações, permitindo tarefas como criação de instâncias EC2, gerenciamento de serviços S3 e RDS, configuração de segurança e permissões, entre outros.

AWS CLI Command Reference: https://docs.aws.amazon.com/cli/latest/index.html

Instalando:

Documentação: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install

Configurando:

    aws configure

Ou

    export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

    export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS>