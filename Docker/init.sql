-- Cria a tabela de produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco NUMERIC(10, 2) NOT NULL,
    estoque INT NOT NULL,
    total_vendas INT DEFAULT 0
);

-- Cria a tabela de atendimentos
CREATE TABLE atendimentos (
    id SERIAL PRIMARY KEY,
    nome_atendente VARCHAR(255) NOT NULL,
    numero_atendimentos INT DEFAULT 0,
    filial VARCHAR(255) NOT NULL
);