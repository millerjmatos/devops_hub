Iniciando serviços no arquivo .yml em background:

    docker-compose up -d

Interrompendo:

    docker-compose down

Interrompendo e removendo os volumes:

    docker-compose down -v

Listando os containers em execução:

    docker-compose ps

Imprimindo logs:

    docker-compose logs

Editando o status:

    docker-compose <stop start restart pause unpause>

Listando as imagens utilizadas:

    docker-compose images

Construindo imagens, caso o Dockerfile tenha sido alterado:

    docker-compose build

Exibindo e validando o arquivo de configuração:

    docker-compose config