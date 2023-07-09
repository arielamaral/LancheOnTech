# LancheOnTech
Projeto de Lanchonete - POS Tech

# Aos professores, seguir os passos para executar a avaliação:
- Clone o repositório.
- Acesse a pasta: LancheOnTech `cd LancheOnTech`
- Altere a branch para fase01: `git checkout fase01`
- Utilize o docker-compose no diretório raiz do projeto `docker-compose up`

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
  "nome": "Batata",
  "preco": 10,
  "descricao": "Acompanhamento"
}

```

Atualizar Produto/preço, utilizar JSON: 

`PUT http://localhost:5000/produto/ID`

```

{
  "nome": "Batata",
  "preco": 10,
  "descricao": "Acompanhamento"
}

```

Deletar Produto

`DELETE http://localhost:5000/produto/ID`

#

*Pedido:*

Consultar todos os pedidos:

`GET http://localhost:5000/pedido/`

Criar Pedido (Necessário utilizar o ID do Produto cadastrado Anteriormente

`POST http://localhost:5000/pedido/`

```
{
    "pedido_id": 1,
    "itens": [
        {
            "produto_id": 1,
            "quantidade": 1
        },
        {
            "produto_id": 2,
            "quantidade": 1
        }

    ]
}
```

Cancelar Pedido:

`DELETE http://localhost:5000/pedido/ID`

# 

*ITEM PEDIDO:*

Deletar items do pedido:

 `DELETE http://localhost:5000/item_pedido/ID DO PRODUTO DENTRO DO PEDIDO`

 #

*PAGAMENTO:*

Efetuar pagamento, necessita enviar JSON:

`POST http://localhost:5000/pagamento/`

```

{
    "pedido_id": 1,
    "metodo_pagamento": "cartao_credito",
    "dados_pagamento": {
        "numero_cartao": "4111111111111111",
        "validade": "12/2023",
        "cvv": "123"
    }
}

```













