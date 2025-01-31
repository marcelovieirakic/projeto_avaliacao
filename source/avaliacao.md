
### Questão: Análise de Dados e Tomada de Decisão

Você foi contratado como analista de dados para uma empresa que possui um banco de dados PostgreSQL com duas tabelas: `produtos` e `atendimentos`. Sua tarefa é realizar uma análise ETL (Extração, Transformação e Carregamento) para responder às seguintes perguntas:

#### Dados das Tabelas:
1. **Tabela `produtos`**:
   - Colunas: `id`, `nome`, `preco`, `estoque`, `total_vendas`.
   - Contém 10 mil linhas de produtos com informações sobre preço, estoque e total de vendas.

2. **Tabela `atendimentos`**:
   - Colunas: `id`, `nome_atendente`, `numero_atendimentos`, `filial`.
   - Contém 10 mil linhas de atendimentos realizados por diferentes atendentes em várias filiais.

#### Tarefas:
1. **Faturamento por Produto**:
   - Calcule o faturamento total de cada produto (faturamento = preço × total_vendas).
   - Identifique o produto que gerou o maior faturamento.

2. **Valor Alocado no Estoque**:
   - Calcule o valor total alocado no estoque de cada produto (valor_estoque = preço × estoque).
   - Identifique o produto com o maior valor alocado no estoque.

3. **Atendimentos por Filial**:
   - Some o número de atendimentos por filial.
   - Identifique as top 5 filiais com o maior número de atendimentos.
   - Gere um gráfico de barras para visualizar as top 5 filiais.

4. **Tomada de Decisão**:
   - Com base nos resultados, responda:
     a) Qual produto deve ser priorizado em campanhas de marketing para aumentar as vendas? Justifique.
     b) Qual filial deve receber mais investimentos em infraestrutura ou treinamento de atendentes? Justifique.
     c) Como você pode otimizar o estoque com base no valor alocado?

#### Requisitos:
- Utilize Python para conectar ao banco de dados, extrair os dados, realizar as transformações e gerar os resultados.
- Use as bibliotecas `psycopg2`, `pandas` e `matplotlib` para a análise e visualização dos dados.
- Apresente os resultados em formato de tabela e gráfico.
- Crie uma classe para cada analise
- pip freeze > requirements.txt necessario para listar todos pacotes do projeto

#### Exemplo de Resposta Esperada:
1. **Faturamento por Produto**:
   - Produto com maior faturamento: "Produto X" com R$ YY,YYY.YY.

2. **Valor Alocado no Estoque**:
   - Produto com maior valor no estoque: "Produto Z" com R$ AA,AAA.AA.

3. **Atendimentos por Filial**:
   - Top 5 filiais: Filial A (XXXX atendimentos), Filial B (YYYY atendimentos), etc.
   - Gráfico de barras das top 5 filiais.

4. **Tomada de Decisão**:
   - a) O produto "Produto X" deve ser priorizado em campanhas de marketing porque gerou o maior faturamento.
   - b) A filial "Filial A" deve receber mais investimentos porque teve o maior número de atendimentos.
   - c) O estoque pode ser otimizado reduzindo o estoque do produto "Produto Z", que tem o maior valor alocado.

---

### Resolução da Questão

A resolução da questão pode ser feita com o código Python fornecido anteriormente. Aqui está um resumo do que o código faz:

1. **Extração**:
   - Conecta ao banco de dados e extrai os dados das tabelas `produtos` e `atendimentos`.
   **Utilizamos o arquivo de configuracao Dockerfile para baixar a imagem e definir variaveis de banco, e na sequencia utilizamos os .sql para criar as tabelas atendimento/produtos e finalizamos populando as tabelas com o script .sql populate**

2. **Transformação**:
   - Calcula o faturamento por produto e identifica o produto com o maior faturamento.
   - Calcula o valor alocado no estoque e identifica o produto com o maior valor.
   - Soma os atendimentos por filial e identifica as top 5 filiais.

3. **Carregamento**:
   - Exibe os resultados em formato de tabela.
   - Gera um gráfico de barras das top 5 filiais.

4. **Tomada de Decisão**:
   - Com base nos resultados, sugere ações como priorização de produtos, investimentos em filiais e otimização de estoque.

---

### Envio da atividade

O código tem que ser enviado através do github e o repositório deverá estar publico na data final da entrega. Será necessário fazer um 
arquivo README.md explicando o passo a passo para execução de seu código.


---