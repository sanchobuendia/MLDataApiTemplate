# API boilerplate

### Clonar o boilerplate
Dentro do diretório de projetos do computador local executar o comando:
```
git clone https://github.com/tradersclub/TCMLApiTemplates.git
```

### Criar projeto

Para criar o projeto é necessário ter o [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/#) na máquina de desenvolvimento.
Dentro do diretório do projeto `TCMLApiTemplates` clonado no passo anterior executar o comando:
```
cookiecutter . -o ~/Projects/<PATH>
```
Algumas perguntas devem ser respondidas para criar o projeto.

### Adicionar o projeto ao GitHub

Criar um repositório no GitHub.
No repositório é necessário adicionar os seguintes secrets:
```
GCP_CREDENTIALS: Adicionar o service account key que está no 1password para o service accoun ci-cd-sa.
GCP_PROJECT: O id do projeto no GCP
```

Dentro do diretório da aplicação criado no passo anterior seguir os passos informados no GitHub para um repositório já existente.

### Estrutura de diretórios
- src => código da aplicação.
  - libraries => diretório com código que pode ser reutilizado entre vários API endpoints. Similar a um Python package
  - models => Modelo de base de dados. Apenas usado para projetos com base de dados.
  - modules => serviços com regras de negócio que serão utilizados pelos API endpoints.
  - routes => API endpoints.
- test => testes da aplicação.
  - modules => testes das regras de negócio.
  - routes => testes de API endpoints.

### Executar a aplicação

Para executar a aplicação e trabalhar no desenvolvimento é necessário ter Docker instalado.
Todo o desenvolvimento é feito usando Docker.
Para iniciar a aplicação executar os comandos:
```
docker-compose build
docker-compose --verbose up
```
Para acessar a aplicação:
http://localhost/api/sum/{num_1}/{num_2} # Aplicação
http://127.0.0.1:5000/swagger/# # Swagger

Ao finalizar o desenvolvimento executar o comando abaixo para terminar o container do Docker:
```
docker-compose --verbose down -v
```

### Executar testes

Para rodar os testes executar os comandos abaixo:
```
docker-compose build
docker-compose run --rm --entrypoint "python -m unittest" app
```

### Modificar código

Antes de modificar o código é uma boa prática criar uma branch no git:
```
git checkout -b <BRANCH>
```

O código de regras de negócio devem ser criados / alterados no caminho ./src/modules/service.py.
O código de API endpoint devem ser criados / alterados no caminho ./src/routes/route.py.
A configuração do Swagger para os endpoints devem ser criados / alterados no caminho ./src/routes/<ENDPOINT>.yaml.

Esses são os únicos locais onde modificações devem ser realizadas.

### Modificar testes

Os testes de regras de negócio devem ser criados / alterados no caminho ./test/modules/service.py.
Os testes de API endpoint devem ser criados / alterados no caminho ./test/routes/route.py.


### Merge to main branch

Quando o trabalho estiver pronto o branch de desenvolvimento deve ser mergeado no branch principal (main/master) no GitHub.

Atualizar o branch principal no computador de desenvolvimento.
```
git checkout main && git pull --rebase origin main
```

### Variáveis de ambiente

Para o ambiente de desenvolvimento as variáveis de ambiente precisam ser criadas no arquivo `.env` na raíz do projeto que será utilizado pelo Docker.

Para produção as variáveis de ambiente devem ser informadas no comando `gcloud` como o exemplo abaixo:
```
gcloud builds submit --config cloudbuild.yaml --substitutions=_ENV_VAR_1="1",_ENV_VAR_2="2" .
```
Essas variáveis precisam ser configuradas no arquivo `cloudbuild.yaml` na raíz do projeto como o exemplo abaixo:
```
steps:
- name: "gcr.io/cloud-builders/docker"
  entrypoint: 'bash'
  args:
  - -c
  - |
    docker buildx build --no-cache -t gcr.io/<TAG> -f Dockerfile.api --build-arg  ENV_VAR_1_ARG=${_ENV_VAR_1} --build-arg ENV_VAR_2_ARG=${_ENV_VAR_2} . --push
```
As variáveis também precisam ser adicionadas no `Dockefile` como o exemplo abaixo:
```
FROM python:3.10.1-slim-buster

WORKDIR /api

ARG ENV_VAR_1_ARG
ENV ENV_VAR_1=$ENV_VAR_1_ARG

ARG ENV_VAR_2_ARG
ENV ENV_VAR_2=$ENV_VAR_2_ARG

...
```

### Deploy

No arquivo `cloudbuild.yaml` a tag deve ser configurada no comando:
```
docker buildx build --no-cache -t gcr.io/<TAG> ...
```

No arquivo `build.yaml` no diretório `.github/workflows` a tag deve ser configurada no passo `Deploy`.
Existem variáveis que devem ser configuradas no início do arquivo:
```
REGION: 
MEMORY:
GCP_APPLICATION:
```

Ao executar o merge com a branch principal (main/master) o deploy ocorrerá automaticamente e uma Cloud Run será criada no projeto GCP informado nos secrets do GitHub.
