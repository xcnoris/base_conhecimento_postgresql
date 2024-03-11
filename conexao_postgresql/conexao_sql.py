import psycopg2 as sql

def conexaosql():
    # Estabelecendo a conexão com o banco de dados
    conexao = sql.connect(database="baseconhecimento",
                        host="localhost",
                        user="postgres",
                        password="123456",
                        port="5432")



    # Retornando a conexão
    return conexao
