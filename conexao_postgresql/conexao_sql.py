import psycopg2 as sql

def conexaosql():
    # Estabelecendo a conexão com o banco de dados
    conexao = sql.connect(database="baseconhecimento",
                        host="******",
                        user="*******",
                        password="*****",
                        port="****")



    # Retornando a conexão
    return conexao
