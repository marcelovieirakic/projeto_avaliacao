import pandas as pd
from sqlalchemy import create_engine
import matplotlib
matplotlib.use('Agg')  # Usa um backend interativo
import matplotlib.pyplot as plt



# Crie a engine de conexão (substitua os valores pelos seus dados de conexão)
engine = create_engine(f'postgresql+psycopg2://meuusuario:minhasenha@localhost:5432/meubanco')

# Leia dados de uma tabela SQL para um DataFrame do Pandas
df_prod = pd.read_sql('produtos', con=engine)
df_atend = pd.read_sql('atendimentos', con=engine)

# Exemplo de consulta SQL personalizada
query_prod = "SELECT * FROM produtos"
query_atend = "SELECT * FROM atendimentos"
df_prod = pd.read_sql(query_prod, con=engine)
df_atend = pd.read_sql(query_atend, con=engine)

# Exibir os dados
# print(df_prod.head())
print(df_atend.head())

# # Criando uma nova coluna 'C' como produto de 'A' e 'B'
# df_prod['faturamento'] = df_prod['preco'] * df_prod['total_vendas']
# df_prod['valor_estoque'] = df_prod['preco'] * df_prod['estoque']

# print(df_prod)

# top_10 = df_prod.nlargest(10, 'faturamento')  # Obtém os 10 maiores valores da coluna 'C'
# top_estoque = df_prod.nlargest(1, 'valor_estoque')  # Obtém os 10 maiores valores da coluna 'C'

# print(top_estoque)

atendimentos_por_filial = df_atend.groupby('filial')['numero_atendimentos'].sum().reset_index().sort_values(by='numero_atendimentos', ascending=False)

top_5_filial = atendimentos_por_filial.nlargest(5, 'numero_atendimentos') 


plt.bar(atendimentos_por_filial['filial'], atendimentos_por_filial['numero_atendimentos'])
plt.xlabel('filial')
plt.ylabel('numero_atendimentos')
plt.title('Top 5 atendimentos por Filial')
plt.savefig("grafico.png")


print(top_5_filial)
