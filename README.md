# Teste Letz (Pokemon - API Trainer)

## Apresentação

Este documento é para apresentar o funcionamento da implementação da rota de treinadores. Foi realizado em python juntamente com o frameworks FLASK, pois por se tratar de um micro-frameworks, instala-se apenas o necessário.

## Autenticação

Esta API está usando como proteção de algumas rotas o JWT.

## Começando

Para acessar a api serão necessários os seguites requisitos:

- [Python 3.9: necessário para a execução do sistema](www.python.org/)
- [Postman: necessário para o teste da API](www.postman.com)

## Desemvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do github em um diretório de sua preferência.

```commandline
mkdir "diretório_de_sua_preferência"
cd "diretório_de_sua_preferência"
git clone https://github.com/mcribeiro27/letz
```

## Construção

Para construir o projeto, execute os comandos abaixo dentro da pasta onde baixou o projeto.

Para ambiente Unix
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirement.txt
```

Para ambiente Windows
```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```
O comando irá montar o ambiente e instalar todos os módulos necessário para  o sistema.

## Configuração

Ao iniciar o sistema teremos que criar o banco de dados, o sistema está configurado para trabalhar com o SQLite.
Para criar o banco execute o seguinte comando:
```commandline
flask create-db
flask run
```
Ao executar sera creado o banco. Apartir daí podemos testar os end-points.

### Trainer
Através desta pasta conseguimos cadastrar, listar, buscar um Trainer na API - Pokemon - Trainers

POST - Para cadastro de um novo trainer
```url
/trainer/
```

BODY:
```json
{
    "nickname": "ash",
    "first_name": "Ash",
    "last_name": "Kutchum",
    "email": "ash@pokemon.com",
    "password": "coxinha123",
    "team": "Team Valor"
}
```
RETORNO:

```json
{
    "id": 1,
    "nickname": "ash",
    "first_name": "Ash",
    "last_name": "Kutchum",
    "email": "ash@pokemon.com",
    "password": "coxinha123",
    "team": "Team Valor",
    "pokemonOwned": 1
}
```
GET - Para listar todos os trainers

```url
/trainer/
```

RETORNO:

```json
{
    "trainers": [
        {
            "id": 1,
            "nickname": "ash",
            "first_name": "Ash",
            "last_name": "Kutchum",
            "email": "ash@pokemon.com",
            "password": "coxinha123",
            "team": "Team Valor",
            "pokemonOwned": 1
        },
        {
            "id": 2,
            "nickname": "ash",
            "first_name": "Ash",
            "last_name": "Kutchum",
            "email": "ash@pokemon.com",
            "password": "coxinha123",
            "team": "Team Valor",
            "pokemonOwned": 1
        }
    ]
}
```
GET by id - Para buscar um trainer especifico.
```url
/trainer/{trainerId}
```
RETORNO:
```json
{
    "id": 1,
    "nickname": "ash",
    "first_name": "Ash",
    "last_name": "Kutchum",
    "email": "ash@pokemon.com",
    "password": "coxinha123",
    "team": "Team Valor",
    "pokemonOwned": 1
}
```

### Pokemon Owned
Através desta pasta conseguimos cadastrar, listar, buscar e deletar um Pokemon Owned na API - Pokemon - Trainers. Obs.: Somente é possivel ter um pokemon owned se existir um trainer.

POST - Para cadastro de um novo Pokemon Owner. Esta rota precisa estar logada para funcionar

```url
/trainer/{trainerId}/pokemon
```

BODY:
```json
{
  "name": "Fluffy",
  "level": 4,
  "pokemon_id": 12
}
```
RESPOSTA:
```json
"pokemons": [
{
    "id": 1,
    "name": "Fluffy",
    "level": 4,
    "pokemon_id": 12,
    "trainer": 1,
    "pokemon_data": {
        ... 
    }
}
```
GET - Para listar todos os pokemons capturado.

```url
/trainer/{trainerId}/pokemon
```

RETORNO:
```json
{
    "pokemons": [
        {
            "id": 1,
            "name": "Fluffy",
            "level": 4,
            "pokemon_id": 12,
            "trainer": 1,
            "pokemon_data": {
                ...
            }
        },
        {
            "id": 2,
            "name": "Fluffy",
            "level": 4,
            "pokemon_id": 12,
            "trainer": 1,
            "pokemon_data": {
                ...
            }
        }
    ]
}
```

GET by id - Para buscar um pokemons capturado especifico.

```url
/trainer/{trainerId}/pokemon/{pokemonId}
```

RETORNO:
```json
{
    "id": 1,
    "name": "Fluffy",
    "level": 4,
    "pokemon_id": 12,
    "trainer": 1,
    "pokemon_data": {
        ...
    }
},
```
DELETE - Para capagar de um Pokemon Owner. Esta rota precisa estar logada para funcionar

```url
/trainer/{trainerId}/pokemon/{pokemonId}
```
RETORNO:
```json
{
    "message": "pokemon 1 deleted"
}
```

## Testes
Lembrando que o banco de dados deve estar criado. Caso não esteja execute o seguinte comando:

```commandline
flask create-db
```

Precisamos ter pelo menos um trainer, para isso executamos o seguinte comando:
```commandline
flask populate-db
```

Todos os testes foram realizados com a biblioteca PYTEST, onde para executar basta rodar no terminal o seguinte comando. 
```commandline
pytest
```
