Comando executado no container:

ENTRYPOINT = command

Argumentos passados para o container:

    CMD = args

### Uso:

    command: ["/bin/sh"]
    args: ["-c", "while true; do echo hello; sleep 10;done"]

Executando um command:

    kubectl run <nome-do-pod> --image nginx --command -- /bin/sh -c "echo 'Olá, Kubernetes!'"

    kubectl run <nome-do-pod> --image nginx --command --dry-run=client -o yaml -- /bin/sh -c env

    kubectl run <nome-do-pod> --image nginx --command --dry-run=client -o yaml -- /bin/sh -c env > command.yaml

Executando:

    kubectl apply -f command.yaml

Verificando os logs:

    kubectl logs command

Modificando:

    kubectl run <nome-do-pod> --image nginx --command --dry-run=client -o yaml -- /bin/sh -c "sleep 1d" > command.yaml

    kubectl apply -f command.yaml --force

Acessando o pod de nome "command":

    kubectl exec -it command -- bash

    apt install procps

    ps aux