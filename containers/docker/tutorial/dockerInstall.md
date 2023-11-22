### Em Debian 11

    cat /etc/os-release

PRETTY_NAME="Debian GNU/Linux 11 (bullseye)" \
NAME="Debian GNU/Linux" \
VERSION_ID="11" \
VERSION="11 (bullseye)" \
VERSION_CODENAME=bullseye \
ID=debian

    uname -r

5.10.0-21-amd64

Realize todo o procedimento como root!

Atualizando o sistema::

    apt-get update && apt-get upgrade -y

Instalando os pré-requisitos:

    apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y

Adicionando a chave GPG oficial do docker ao sistema:

    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

Adicionando o repositório do docker ao sources.list.d:

    echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list

Atualizando o repositório:

    apt-get update

Instalando:

    apt-get install docker-ce docker-ce-cli containerd.io -y

Verificando o serviço:

    systemctl status docker