# API LATAM

API criada para consumo e criação de cards e coluna no kanbam

## Tecnologias Utilizadas

A API foi criada com as seguintes tecnologias:

- [Python] - Linguagem Principal
- [Fast API] - Framework utilizado para criação da API
- [MySQL] -Banco utilizado para armazenamento das informações.


## Instalação

Primeiro passo e baixar o repositorio no GitHub: https://github.com/higorsoares17/latam

Em seguida criar um ambiente virtual
```sh
python -m venv "nome_do_ambiente"
```
Logo após criar um arquivo .env, seguindo como padrão o arquivo .env-example

Após ter criado o arquivo .env, instalar as blibliotecas da API
```sh
pip install -r requirements.txt
```

Logo em seguida  instalar e iniciar o Mysql, você pode baixar e instalar atraves do link: https://dev.mysql.com/downloads/mysql/

Em seguida prencher o .env com os dados da conexão do MySql.

Com os passos acima feitos basta  rodar a aplicação com o seguinte comando:

```sh
uvicorn main:app
```

## Documentação

Toda documentação do projeto estra presente acessando "localhost/docs" ou "localhost/redocs".

Lá você vai encontrar todas as rotas da aplicação e podera realizar todos testes do CRUD em cada Rota.


