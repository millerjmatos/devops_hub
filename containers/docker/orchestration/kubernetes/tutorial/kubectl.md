O kubectl é a principal ferramenta de linha de comando do Kubernetes, usada para interagir e gerenciar clusters Kubernetes. Com o kubectl, os administradores e desenvolvedores podem implantar, dimensionar e gerenciar contêineres e recursos do Kubernetes, bem como verificar o estado de pods, serviços, deployments e outros componentes do cluster.

Documentação: https://kubernetes.io/docs/reference/kubectl/

### Instalando o kubectl:

Documentação: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

Baixando a ferramenta de linha de comando do kubernetes:

    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

    chmod +x kubectl
        
    sudo mv kubectl /usr/local/bin/

Criando o primeiro pod:

    kubectl run <nome-do-pod> --image <imagem:tag>

    kubectl run primeiro-pod --image nginx:latest

Verificando antes criar:

    kubectl run nginx --image nginx -o yaml --dry-run=client

Criando o pod com a saída do manifesto:

    kubectl run <nome-do-pod> --image nginx -o yaml --dry-run=client > <nome-do-arquivo>.yaml
    
    kubectl apply -f <nome-do-arquivo>.yaml

Imprimindo informações sobre os pods em execução:

    kubectl get pods

    kubectl get pods --watch

    kubectl get pods -o wide

Examinando o pod:

    kubectl describe pod <nome-do-pod>

    kubectl get pod <nome-do-pod> -o yaml

Fazendo replace de um pod após a edição, maneira rápida:

    kubectl replace -f pod.yaml --force --grace-period 0

Editando o pod:

    kubectl edit pod <nome-do-pod>

    kubectl get pod nome-do-pod -o yaml > pod.yaml ; vim pod.yaml

Todas as opções de um pod:

    kubectl explain pod

    kubectl explain pod.spec

    kubectl explain pod.spec --recursive

Deletando o pod criado de maneira imperativa:

    kubectl delete pod nome-do-pod

    kubectl delete pod nome-do-pod --force --grace-period 0

    kubectl delete pods --all

Deletando o pod criado de maneira declarativa:

    kubectl delete -f ./primeiro-pod.yaml

Executando um comando dentro de um pod:

    kubectl exec -it <nome-do-pod> -- <comando>

    kubectl exec -it <nome-do-pod> --container <nome-do-container> -- <comando>

    kubectl exec -it <nome-do-pod> -c <nome-do-container> -- <comando>

        curl localhost:80

Imprimindo informações do cluster:

    kubectl cluster-info

    kubectl api-resources

Imprimindo informações sobre os nós do cluster:

    kubectl get nodes

Imprimindo logs de um pod:

    kubectl logs <nome-do-pod>