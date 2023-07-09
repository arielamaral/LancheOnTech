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

![CONSULTAR_CLIENTES](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CONSULTA_CLIENTE.png)

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

![CADASTRAR_CLIENTES](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CADASTRA_CLIENTE.png)

Atualizar cliente, utilizar JSON: 

`PUT http://localhost:5000/cliente/ID`

```
{
  "cpf": "111111111112",
  "email": "cliente02@ariel.fiap",
  "nome": "Cliente 02"
}
```

![ATUALIZAR_CLIENTE](https://github.com/arielamaral/LancheOnTech/blob/endpoints/ATUALIZA_CLIENTE.png)

Deletar cliente

`DELETE http://localhost:5000/cliente/ID`

![DELETAR_CLIENTE](https://github.com/arielamaral/LancheOnTech/blob/endpoints/DELETA_CLIENTE.png)

***ID's disponíveis com o GET***

#

*Produtos:*

Consultar todos os produtos/preços

`GET http://localhost:5000/produto/`

![CONSULTAR_PRODUTO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CONSULTAR_PRODUTOS.png)

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

![CADASTRAR_PRODUTO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CADASTRAR_PRODUTO.png)

Atualizar Produto/preço, utilizar JSON: 

`PUT http://localhost:5000/produto/ID`

```

{
  "nome": "Batata",
  "preco": 10,
  "descricao": "Acompanhamento"
}

```

![ATUALIZAR_PRODUTO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/ATUALIZAR_PRODUTO.png)

Deletar Produto

`DELETE http://localhost:5000/produto/ID`

![DELETAR_PRODUTO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/DELETAR_PRODUTO.png)

#

*Pedido:*

Consultar todos os pedidos:

`GET http://localhost:5000/pedido/`

![CONSULTAR_PEDIDOS](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CONSULTAR_PEDIDO.png)

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
![CRIAR PEDIDO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CRIAR_PEDIDO.png)

Cancelar Pedido:

`DELETE http://localhost:5000/pedido/ID`

![CANCELAR_PEDIDO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/CANCELAR_PEDIDO.png)

# 

*ITEM PEDIDO:*

Deletar items do pedido:

 `DELETE http://localhost:5000/item_pedido/ID DO PRODUTO DENTRO DO PEDIDO`

 ![DELETAR_ITEM_PEDIDO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/REMOVER_ITEM_PEDIDO.png)

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
![PAGAMENTO](https://github.com/arielamaral/LancheOnTech/blob/endpoints/PAGAMENTO_PEDIDO.png)
