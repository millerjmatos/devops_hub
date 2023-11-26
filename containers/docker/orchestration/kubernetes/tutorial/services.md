Os serviços fornecem uma maneira de expor aplicativos em execução dentro dos pods para outros serviços ou usuários. Um serviço define uma política de acesso ao conjunto de pods e oferece uma interface estável para acessar os pods, mesmo que eles sejam escalados ou reimplantados.

Documentação: https://kubernetes.io/docs/concepts/services-networking/service/

**ClusterIP:**

É usado para comunicação interna dentro do cluster. 

**NodePort:**

É usado para acesso externo a um cluster, embora não seja recomendado para produção.

**LoadBalancer:**

É usado quando você precisa distribuir o tráfego entre várias instâncias do aplicativo em um ambiente escalável. Utilizam automaticamente os balanceadores de carga de cloud providers. Por serem um Load Balancer, também são um NodePort e ClusterIP ao mesmo tempo: 

*A escolha do tipo de serviço depende das necessidades específicas do seu aplicativo e do ambiente em que está sendo implantado.*

Expondo um pod:

    kubectl expose pod <nome-do-pod> --type NodePort --port 80 --target-port <30000-32767> --name <nome-do-svc>

`--type` se omitido o default é ClusterIP

`--target-port` pode ser omitido, uma porta aleatória para o pod será reservada

Expondo um deployment:

    kubectl expose deployment <nome-do-deployment> --type NodePort --name <nome-do-svc>