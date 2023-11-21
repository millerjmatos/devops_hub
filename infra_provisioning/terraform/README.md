O Terraform é uma ferramenta de código aberto para provisionamento e gerenciamento de infraestrutura como código (IaC). Com o Terraform, é possível descrever a infraestrutura desejada em um arquivo de configuração declarativo, especificando recursos e suas dependências. Ele suporta diversos provedores de nuvem, como AWS, Azure, Google Cloud, entre outros, permitindo que as equipes definam, versionem e compartilhem a infraestrutura de forma eficiente. Ao executar o Terraform, ele cria, altera ou destrói os recursos de maneira automática e segura, garantindo que o estado real da infraestrutura esteja sempre de acordo com a definição do código, facilitando o gerenciamento e a escalabilidade de ambientes.

Documentação: https://developer.hashicorp.com/terraform

#### Instalação:

https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli

ou:

    cd /tmp/

    wget https://releases.hashicorp.com/terraform/1.6.2/terraform_1.6.2_linux_386.zip

    unzip terraform_*.zip

    sudo mv terraform /usr/local/bin/

    terraform --version