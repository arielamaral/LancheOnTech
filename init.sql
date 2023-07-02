CREATE TABLE Cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE
);

CREATE TABLE Produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(200) NOT NULL,
    preco FLOAT NOT NULL
);

CREATE TABLE Pedido (
    id SERIAL PRIMARY KEY,
    valor_total FLOAT NOT NULL
);

CREATE TABLE "Item_Pedido" (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(id),
    FOREIGN KEY (produto_id) REFERENCES Produto(id)
);