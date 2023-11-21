Como o nome diz, o volume emptyDir está inicialmente vazio. Todos os contêineres no Pod podem ler e gravar os mesmos arquivos no volume emptyDir, embora esse volume possa ser montado no mesmo caminho ou em caminhos diferentes em cada contêiner. Quando um Pod é removido de um nó por qualquer motivo, os dados no emptyDir são eliminados permanentemente.

Documentação: https://kubernetes.io/pt-br/docs/concepts/storage/volumes/#emptydir
