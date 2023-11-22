O Docker Compose não é necessário para executar conteiners do docker, mas é uma ferramenta útil para simplificar a orquestração de conteiners em ambientes de desenvolvimento e produção. Isso é útil para aplicativos que exigem vários conteiners trabalhando juntos, como aplicativos web que exigem um contêiner para o servidor web, um contêiner para o banco de dados e um contêiner para o serviço de cache.

Verifique a versão mais recente do docker compose disponível em https://github.com/docker/compose/releases e substitua a versão na URL:

    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose

    chmod +x /usr/local/bin/docker-compose

    docker-compose --version