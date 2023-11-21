Um cluster de Kubernetes é composto por um conjunto de máquinas chamadas de nós. Cada nó é uma máquina virtual ou física que executa o Kubernetes e é responsável por executar conteiners.

No Kubernetes, o Master Node (Control Plane) é composto por vários componentes, cada um com uma função específica: api server, etcd, controller manager e scheduler. O master coordena os nós de trabalho (Worker Nodes) onde conteiners são realmente executados. 

Instalando o minikube:

Documentação: https://minikube.sigs.k8s.io/docs/start/

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

    chmod +x minikube

    sudo mv minikube /usr/local/bin/

Iniciando cluster local:

    minikube start --driver=docker

Imprimindo informações do cluster:

    minikube status

    kubectl cluster-info

    docker ps -a