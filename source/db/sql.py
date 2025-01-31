import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
import pandas as pd

class PostgresConnector:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PostgresConnector, cls).__new__(cls)
        return cls._instance

    def __init__(self, host, database, user, password, port=5432):
        """
        Inicializa o conector para o banco de dados PostgreSQL.

        :param host: Endereço do servidor PostgreSQL.
        :param database: Nome do banco de dados.
        :param user: Usuário para autenticação.
        :param password: Senha para autenticação.
        :param port: Porta do servidor PostgreSQL (padrão: 5432).
        """
        if not hasattr(self, "_initialized"):
            self.host = host
            self.database = database
            self.user = user
            self.password = password
            self.port = port
            self.connection = None
            self._initialized = True

    def connect(self):
        """Estabelece a conexão com o banco de dados."""
        if not self.connection:
            try:
                self.connection = psycopg2.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password,
                    port=self.port
                )
            except psycopg2.Error as e:
                raise Exception(f"Erro ao conectar ao banco de dados: {e}")

    def execute_query(self, query, params=None):
        """
        Executa uma consulta SQL no banco de dados.

        :param query: Consulta SQL para executar.
        :param params: Parâmetros para a consulta (opcional).
        :return: Resultado da consulta para SELECT, ou None para outros comandos.
        """
        if not self.connection:
            raise Exception("Conexão não estabelecida. Chame o método 'connect' primeiro.")

        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                cursor.execute(query, params)
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                self.connection.commit()
            except psycopg2.Error as e:
                self.connection.rollback()
                raise Exception(f"Erro ao executar a consulta: {e}")

    def validate_columns(self, table, columns):
        """
        Valida se as colunas fornecidas existem na tabela.

        :param table: Nome da tabela.
        :param columns: Lista de colunas para validar.
        :return: None. Lança uma exceção se alguma coluna não existir.
        """
        if not self.connection:
            raise Exception("Conexão não estabelecida. Chame o método 'connect' primeiro.")

        query = """
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = %s
        """
        result = self.execute_query(query, (table,))
        valid_columns = {row['column_name'] for row in result}

        for column in columns:
            if column not in valid_columns:
                raise Exception(f"A coluna '{column}' não existe na tabela '{table}'.")

    def select(self, table, columns="*", where_clause=None, params=None):
        """
        Executa um SELECT no banco de dados com validação de colunas.

        :param table: Nome da tabela.
        :param columns: Colunas a serem retornadas (lista ou "*").
        :param where_clause: Cláusula WHERE opcional.
        :param params: Parâmetros para a cláusula WHERE.
        :return: Resultado da consulta.
        """
        if columns != "*":
            self.validate_columns(table, columns)
            columns = ", ".join(columns)

        query = f"SELECT {columns} FROM {table}"
        if where_clause:
            query += f" WHERE {where_clause}"

        return self.execute_query(query, params)

    def update(self, table, updates, where_clause=None, params=None):
        """
        Executa um UPDATE no banco de dados com validação de colunas.

        :param table: Nome da tabela.
        :param updates: Dicionário com as colunas e valores a serem atualizados.
        :param where_clause: Cláusula WHERE opcional.
        :param params: Parâmetros para a cláusula WHERE.
        """
        self.validate_columns(table, updates.keys())

        set_clause = ", ".join([f"{col} = %s" for col in updates.keys()])
        query = f"UPDATE {table} SET {set_clause}"
        if where_clause:
            query += f" WHERE {where_clause}"

        self.execute_query(query, list(updates.values()) + (params or []))

    def delete(self, table, where_clause=None, params=None):
        """
        Executa um DELETE no banco de dados.

        :param table: Nome da tabela.
        :param where_clause: Cláusula WHERE opcional.
        :param params: Parâmetros para a cláusula WHERE.
        """
        if where_clause:
            query = f"DELETE FROM {table} WHERE {where_clause}"
            self.execute_query(query, params)
        else:
            raise Exception("DELETE sem cláusula WHERE não é permitido.")

    def save_dataframe_to_table(self, df, table_name, if_exists="append"):
        """
        Salva um DataFrame do Pandas em uma tabela do banco de dados.

        :param df: DataFrame do Pandas a ser salvo.
        :param table_name: Nome da tabela no banco de dados.
        :param if_exists: Comportamento se a tabela já existir:
            - 'fail': Lança uma exceção.
            - 'replace': Sobrescreve a tabela.
            - 'append': Adiciona os dados à tabela existente.
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("O argumento 'df' deve ser um DataFrame do Pandas.")

        # Cria a conexão SQLAlchemy para integração com o Pandas
        engine = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        )

        try:
            df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
        except Exception as e:
            raise Exception(f"Erro ao salvar o DataFrame na tabela '{table_name}': {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
            except psycopg2.Error as e:
                raise Exception(f"Erro ao fechar a conexão: {e}")
