Ele permite que você defina como um aplicativo deve ser implantado, qual imagem usar, quantas réplicas devem estar em execução e como as atualizações devem ser tratadas. Além disso, o Deployment fornece suporte a rollbacks de atualizações e ações de pausa/retomada de rollouts.

Uma notável diferença entre um Deployment e um ReplicaSet é que o primeiro realiza as alterações automaticamente após a modificação do arquivo de configuração.

Documentação: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

Histórico de atualizações:

    kubectl rollout history deployment nome_do_deployment

Gravando a alteração no histórico:

    kubectl apply -f ./nome_do_deployment.yaml --record

Commit:

    kubectl annotate deployment nome_do_deployment kubernetes.io/change-cause="Primeiro commit!"

ou via arquivo de configuração:

    kubernetes.io/change-cause: seu_commit

Rollback para a gravação 2:

    kubectl rollout undo deployment nome_do_deployment --to-revision=2

Imprimindo o status do deployment:

    kubectl rollout status deployment nome_do_deployment

Pausando, editando e retomando o deployment:

    kubectl rollout pause deployment nome_do_deployment

    kubectl edit deployment nome_do_deployment 

    kubectl rollout resume deployment nome_do_deployment