## 1. kubectl: Principal Ferramenta de Linha de Comando do Kubernetes:

O kubectl é essencial para administrar clusters Kubernetes, permitindo implantação, escalonamento e gerenciamento de contêineres e recursos.

Documentação: https://kubernetes.io/docs/reference/kubectl/

## 2. Instalação do kubectl:

Documentação: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/

## 3. Criando o Primeiro Pod:

    kubectl run primeiro-pod --image nginx:latest
    kubectl run nginx --image nginx -o yaml --dry-run=client
    kubectl run <nome-do-pod> --image nginx -o yaml --dry-run=client > <nome-do-arquivo>.yaml
    kubectl apply -f <nome-do-arquivo>.yaml

## 4. Verificando e Examinando Pods:

    kubectl get pods
    kubectl get pods -w
    kubectl get pods -o wide
    kubectl get pods -A
    kubectl describe pod <nome-do-pod>
    kubectl get pod <nome-do-pod> -o yaml

## 5. Edição e Substituição de Pods:

    kubectl replace -f pod.yaml --force --grace-period 0
    kubectl edit pod <nome-do-pod>

## 6. Explorando Configurações de Pods:

    kubectl explain pod
    kubectl explain pod.spec
    kubectl explain pod.spec --recursive

## 7. Deletando Pods:

    kubectl delete pod <nome-do-pod>
    kubectl delete pod <nome-do-pod> --force --grace-period 0
    kubectl delete pods --all
    kubectl delete -f ./primeiro-pod.yaml

## 8. Execução de Comandos em Pods:

    kubectl exec -it <nome-do-pod> -- <comando>
    kubectl exec -it <nome-do-pod> --container <nome-do-container> -- <comando>
    kubectl exec -it <nome-do-pod> -c <nome-do-container> -- <comando>

## 9. Informações do Cluster e Nós:

    kubectl cluster-info
    kubectl api-resources
    kubectl get nodes

## 10. Logs de um Pod:

    kubectl logs <nome-do-pod>

## 11. Escalonamento de Pods:

    kubectl scale deployment <nome-do-deployment> --replicas=<número-de-replicas>
    kubectl autoscale deployment <nome-do-deployment> --min=<min-replicas> --max=<max-replicas> --cpu-percent=<percentual-de-uso-da-cpu>

## 12. Atualização de Imagens de Containers:

    kubectl set image deployment/<nome-do-deployment> <nome-do-container>=<nova-imagem:tag>

## 13. Secrets e ConfigMaps:

    kubectl create secret generic <nome-do-secret> --from-literal=key1=value1 --from-literal=key2=value2
    kubectl create configmap <nome-do-configmap> --from-literal=key1=value1 --from-literal=key2=value2

## 14. Gerenciamento de Namespaces:

    kubectl create namespace <nome-do-namespace>
    kubectl get namespaces
    kubectl get all -n <nome-do-namespace>

## 15. Monitoramento de Recursos:

    kubectl top pods
    kubectl top nodes

## 16. Trabalhando com Volumes e Storage Classes:

    kubectl create storageclass <nome-da-storageclass> --provisioner=<provisioner> --dry-run=client -o yaml
    kubectl get storageclass
    kubectl describe storageclass <nome-da-storageclass>

    kubectl create pv <nome-do-pv> --capacity=<tamanho-do-armazenamento> --access-modes=<modos-de-acesso> --storage-class=<nome-da-storageclass> --host-path=/caminho/no/nodo --dry-run=client -o yaml
    kubectl get pv
    kubectl describe pv <nome-do-pv>

    kubectl create pvc <nome-do-pvc> --access-modes=<modos-de-acesso> --storage-class=<nome-da-storageclass> --resources=requests.storage=<tamanho-do-armazenamento> --dry-run=client -o yaml
    kubectl get pvc
    kubectl describe pvc <nome-do-pvc>

## 17. Acesso a Pods via Port Forwarding: 

    kubectl port-forward <nome-do-pod> <porta-local>:<porta-no-pod>

## 18. Backup e Restauração de Recursos:

    kubectl get all --all-namespaces -o yaml > backup.yaml
    kubectl apply -f backup.yaml

## 19. RBAC (Role-Based Access Control):

    kubectl create serviceaccount <nome-da-service-account>
    kubectl create clusterrolebinding <nome-da-binding> --clusterrole=<nome-do-cluster-role> --serviceaccount=<namespace>:<nome-da-service-account>

## 20. Troubleshooting:

    kubectl describe pod <nome-do-pod>
    kubectl logs <nome-do-pod> -c <nome-do-container>
    kubectl get events

## 21. Expondo Pods e Deployments:

    kubectl expose pod <nome-do-pod> --port <porta-no-svc> --target-port <porta-no-pod-30000-32767> --name <nome-do-svc> --type <tipo-do-svc>
    kubectl expose deployment <nome-do-deployment> --port <porta-no-svc> --target-port <porta-no-pod-30000-32767> --name <nome-do-svc> --type <tipo-do-svc>
    kubectl get endpoints <nome-do-svc>

## 22. Gerenciando Deployments:

    kubectl create deployment <nome-do-deployment> --image <nome-da-imagem> --replicas 3 --dry-run=client -o yaml
    kubectl rollout history deployment <nome-do-deployment>
    kubectl apply -f ./nome_do_deployment.yaml --record
    kubectl annotate deployment <nome-do-deployment> kubernetes.io/change-cause="Primeiro commit!"
    kubectl rollout undo deployment <nome-do-deployment> --to-revision=2
    kubectl rollout status deployment <nome-do-deployment>
    kubectl rollout pause deployment <nome-do-deployment>
    kubectl edit deployment <nome-do-deployment>
    kubectl rollout resume deployment <nome-do-deployment>

## 23. Entrypoint e Argumentos em Containers:

    kubectl run <nome-do-pod> --image nginx --command -- /bin/sh -c "echo 'Olá, Kubernetes!'"
    kubectl run <nome-do-pod> --image nginx --command --dry-run=client -o yaml -- /bin/sh -c env
    kubectl run <nome-do-pod> --image nginx --command --dry-run=client -o yaml -- /bin/sh -c env > command.yaml
    kubectl apply -f command.yaml

## 24 Ingress

    kubectl create ingress <nome-do-ingress> --rule="<hostname-do-ingress>/<path-no-ingress>=<nome-do-servico>:<porta-do-servico>" --dry-run=client -o yaml
    kubectl get ingresses
    kubectl describe ingress <nome-do-ingress>
