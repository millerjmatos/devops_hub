Um PersistentVolumeClaim (PVC) é uma solicitação de armazenamento por um usuário. É semelhante a um pod. Os pods consomem recursos do nó e os PVCs consomem recursos PV.

#### Resources:

Como pods, podem solicitar quantidades específicas de um recurso. Nesse caso, a solicitação é para armazenamento.

    resources:
      requests:
        storage: 5Gi
