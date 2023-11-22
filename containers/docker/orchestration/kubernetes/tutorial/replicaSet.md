Um ReplicaSet é um recurso para garantir que um número específico de réplicas (pods) de um aplicativo esteja sempre em execução no nó. Ele monitora o estado dos pods garantindo o número desejado de réplicas seja mantido, reiniciando ou substituindo os pods conforme necessário. 

O ReplicaSet é útil para manter a alta disponibilidade de aplicativos, garantindo que, se algum pod falhar, outro pod seja criado automaticamente para substituí-lo e manter o estado desejado do aplicativo.

Documentação: https://kubernetes.io/pt-br/docs/concepts/workloads/controllers/replicaset/