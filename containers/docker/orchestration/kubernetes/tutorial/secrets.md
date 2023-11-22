Kubernetes Secrets permitem armazenar e gerenciar informações confidenciais, como senhas, tokens OAuth e chaves SSH. Armazenar informações confidenciais em um secret é mais seguro e flexível do que colocá-las literalmente em uma definição de pod ou em uma imagem de contêiner.

Uma secret pode ser utilizada com um pod de três maneiras:

Como arquivos em um volume montado em um ou mais de seus contêineres.
Como variável de ambiente do contêiner.
Kubelet para fazer o pulling imagens para um Pod.

Base64:

    echo -n 'admin' | base64

    echo -n 'senhasegura' | base64

Decode:

    echo -n <secret_base64> | base64

Criação em modo rápido:

    kubectl create secret generic minha-secret --from-literal=user=admin --from-literal=pass=senhasegura
