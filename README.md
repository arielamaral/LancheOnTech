# LancheOnTech
Projeto de Lanchonete - POS Tech

# Aos professores, seguir os passos para executar a avaliação:
- Clone o repositório.
- Altere a branch para fase01: `git checkout fase01`
- Utilize o docker-compose `docker-compose up`

***Toda a documentação da Fase01, está diponível na branch: `fase01`

Obs: A base de dados está vazia, é necessário efetuar a criação do: Cliente, Produto e Pagamento.

#

***Endpoints***

*Cliente:*

Consultar todos os clientes:

`GET http://localhost:5000/cliente/`

Consultar cliente especifico:

`GET http://localhost:5000/cliente/ID`

Cadastrar cliente, utilizar JSON: 

`POST http://localhost:5000/cliente/`

```
{
  "cpf": "111111111111",
  "nome": "Cliente 01",
  "email": "cliente01@ariel.fiap"
}
```

Atualizar cliente, utilizar JSON: 

`PUT http://localhost:5000/cliente/ID`

```
{
  "cpf": "111111111112",
  "email": "cliente02@ariel.fiap",
  "nome": "Cliente 02"
}
```

Deletar cliente

`DELETE http://localhost:5000/cliente/ID`

***ID's disponíveis com o GET***

#

*Produtos:*

Consultar todos os produtos/preços

`GET http://localhost:5000/produto/`

Consultar  produtos/preços específicos

`GET http://localhost:5000/produto/ID`

Cadastrar Produto/preço, utilizar JSON: 

`POST http://localhost:5000/produto/`

```

{
    "nome": "Hamburguer",
    "preco": 20,
    "descricao": "Lanche"
}

```

Atualizar Produto/preço, utilizar JSON: 

`PUT http://localhost:5000/produto/ID`

```

{
    "nome": "Hamburguer",
    "preco": 20,
    "descricao": "Lanche"
}

```

Deletar Produto

`DELETE http://localhost:5000/produto/ID`

#




