Um pod é a unidade básica no kubernetes e representa um ou mais conteiners agrupados. Geralmente, os conteiners dentro de um pod compartilham recursos e se comunicam entre si via localhost. Os pods são escaláveis e distribuídos em vários nós para garantir alta disponibilidade.

Documentação: https://kubernetes.io/docs/concepts/workloads/pods/

Criando um arquivo .yaml com:

    mkdir -p /home/muller/k8s ; cd /home/muller/k8s && touch primeiro-pod.yaml && vim primeiro-pod.yaml

Cole:

    apiVersion: v1
    kind: Pod
    metadata:
        name: primeiro-pod
    spec:
    containers:
        - name: container-pod
        image: nginx:latest

Acessar a pasta do arquivo e aplicar:

    kubectl apply -f ./primeiro-pod.yaml

Ao usar arquivos YAML para definir recursos no Kubernetes, como pods, serviços, deployments, etc., você pode fazer alterações nesses arquivos e aplicá-los novamente para atualizar ou modificar os recursos no cluster.