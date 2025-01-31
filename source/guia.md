No terminal, navegue até o diretório do projeto e execute os seguintes comandos:

Construa a imagem Docker:

docker build -t meu-postgres .

Execute o contêiner:

docker run -d --name meu-postgres-container -p 5432:5432 meu-postgres

Isso vai:

Criar um banco de dados chamado meubanco.

Criar um usuário meuusuario com senha minhasenha.

Criar as tabelas produtos e atendimentos.

Popular cada tabela com 10 mil linhas.

Persistência de Dados:

Se quiser persistir os dados fora do contêiner, use volumes Docker:

docker run -d --name meu-postgres-container -p 5432:5432 -v meu-volume:/var/lib/postgresql/data meu-postgres