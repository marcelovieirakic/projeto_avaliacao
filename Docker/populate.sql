-- Insere 10 mil produtos
DO $$
BEGIN
    FOR i IN 1..10000 LOOP
        INSERT INTO produtos (nome, preco, estoque, total_vendas)
        VALUES (
            'Produto ' || i,
            (random() * 1000)::NUMERIC(10, 2),
            (random() * 100)::INT,
            (random() * 500)::INT
        );
    END LOOP;
END $$;

-- Insere 10 mil atendimentos
DO $$
BEGIN
    FOR i IN 1..10000 LOOP
        INSERT INTO atendimentos (nome_atendente, numero_atendimentos, filial)
        VALUES (
            'Atendente ' || i,
            (random() * 100)::INT,
            'Filial ' || (random() * 10)::INT
        );
    END LOOP;
END $$;