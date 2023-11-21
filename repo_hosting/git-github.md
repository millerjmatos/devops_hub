Instalando o git:

	apt install git

Checando a versão:

	git version

Configuração básica para os commits:

	git config --global user.name "Muller Jorge"

	git config --global user.email "contato@mullertec.com.br"

	git config user.name

	git config user.email

Clonando um repositório do github localmente:

	git clone https://github.com/user/<nome_do_repositorio>.git

Atualizando o repositório local:

	git pull

Se o branch local estiver atrás do branch remoto e que há submissões diferentes em cada um:

	git pull origin main

Imprimindo todas as modificações:

	git status

Adicionando as mudanças ao repositório local:

	git add .

Salvando o estado atual do repositório:

	git commit -m "mensagem"

Enviando os dados para o github:

	git push

Imprimindo os logs:

	git log --oneline

	git log -p

Descartando todas as alterações locais:

	git restore .

Voltando para um determinado momento e enviando:

	git restore --source <commit_code> .

	git commit . -m "mensagem"
	
	git push

Criando uma branch e alterando a localização:

	git checkout -b <name_branch>

Listando os branches e a localização:

	git branch

Trocando de branch:

	git switch <main|name_branch>

Enviando os dados para o branch específico:

	git push origin <name_branch>

Mesclando a branch principal com a title e atualizando:

	git switch main

	git merge <title_branch>

	git push origin main

Mesclando a branch e seu histórico de commits:

	git rebase <tittle_branch>

Desfazendo alterações após 'git add':

	git reset HEAD <file_name>

	git checkout -- <file_name>

Desfazendo após commit:

	git log

	git revert 6991813e12a26b9ecb6898554732c90c

		:x

	git log

Viajando no tempo:

	git checkout 69918

	git log --oneline

Voltando para o estado atual:

	git checkout main

Corrigindo o último commit:

	git commit --amend -m "new commit"

	git push origin main --force
