Um ConfigMap é um objeto API usado para armazenar dados não confidenciais em chave-valor. Não é criptografado.

Existem quatro maneiras diferentes de usar um ConfigMap para configurar um contêiner dentro de um pod:

Dentro de um comando de container e args
Variáveis ​​de ambiente para um container
Volumes
Utilizando a API do Kubernetes

Documentação: https://kubernetes.io/docs/concepts/configuration/configmap/

Criando no modo rápido:

    kubectl create cm  primeiro-cm --from-literal=ip=10.0.0.2 --from-literal=tier=web --dry-run=client -o yaml

Direcionando a saída e criando:

    kubectl create cm  primeiro-cm --from-literal=ip=10.0.0.2 --from-literal=tier=web --dry-run=client -o yaml > env1.config

    kubectl apply -f env1.config

Criando o cm através de um arquivo de configuração:

    vim config.txt

        config.database=mysql
        config.database_ip=10.0.0.10

    :x

Criando o cm através do arquivo config.txt:

    kubectl create cm segundo-cm --from-file=config.txt --dry-run=client -o yaml

Direcionando a saída e criando:

    kubectl create cm segundo-cm --from-file=config.txt --dry-run=client -o yaml > env2.config

    kubectl apply -f env2.config

Editando:

    kubectl edit <configMap-name>

Após editar o cm é preciso reiniciar o pod para surgir o efeito!