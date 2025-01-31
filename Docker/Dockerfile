# Usa a imagem oficial do PostgreSQL
FROM postgres:latest

# Define variáveis de ambiente para o PostgreSQL
ENV POSTGRES_DB=meubanco
ENV POSTGRES_USER=meuusuario
ENV POSTGRES_PASSWORD=minhasenha

# Copia os scripts de inicialização para o contêiner
COPY init.sql /docker-entrypoint-initdb.d/
COPY populate.sql /docker-entrypoint-initdb.d/