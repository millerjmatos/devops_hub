Criando um container e executando:

	docker run ubuntu

Criando e executando um comando em modo interativo:

	docker run -it ubuntu bash

Criando um container e executando em background (detached):

	docker run -d dockersamples/static-site

Criando um container em background e mapeando todas as portas:

	docker run -d -P dockersamples/static-site

Criando um container em background e mapeando portas específicas:

	docker run -d -p 8080:80 dockersamples/static-site

Imprimindo as portas mapeadas do container:

	docker port 91382406ec

Imprimindo os containers ativos:

	docker ps

Imprimindo todos os containers:

	docker ps -a

Parando um container:

	docker stop 91382406ec

Parando um container imediatamente:

	docker stop -t=0 91382406ec

Iniciando:

	docker start 91382406ec

Executando um comando com o container:

	docker exec -it 91382406ec bash

	exit

Menos agressivo que o stop:

	docker <pause unpause> 91382406ec

Removendo o container:

	docker rm 91382406ec

Removendo o container em execução:

	docker rm 91382406ec --force

Imprimindo as imagens locais:

	docker images

Imprimindo informações de uma imagem:

	docker <inspect history> 91382406ec

Removendo uma imagem:

	docker rmi 91382406ec

Pesquisando imagens por nome:

	docker search httpd

Logando no docker hub:

	docker login -u username

Renomeando a imagem:

	docker tag local-image:tagname new-repo:tagname

Enviando:

	docker push new-repo:tagname

Removendo vários containers:

	docker container rm $(docker container ls -aq)

Removendo todos os containers parados:

	docker container prune -f

Removendo várias imagens:

	docker rmi $(docker image ls -aq)

Criando uma imagem:

No diretório atual, onde está o arquivo Dockerfile.

	docker build -t local-image:tagname .

Criando um volume:

	docker volume create meu-volume-ubuntu

Mapeando o volume:

Em /var/lib/docker/

	docker run -it -v meu-volume-ubuntu:/dir ubuntu bash

Usando o mount:

	docker run -it --mount type=bind,source=meu-novo-volume-ubuntu,target=/dir ubuntu bash

Imprimindo as redes que o docker já tem no sistema:

	docker network ls

Criando uma rede:

	docker network create --driver bridge minha-bridge