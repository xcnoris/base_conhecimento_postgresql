from conexao_postgresql.conexao_sql import conexaosql
from abas_de_funcoes.exibir_subtitulo import exibir_subtitulo

import os

def remover_conhecimento():
    os.system('cls')

    try:
        exibir_subtitulo('Remover conhecimento')
        id_conhecimento = int(input('Digite o id do conhecimento que voce deseja remover: '))
    except ValueError:
        input('\nO ID do conhecimento deve ser um número inteiro.')
    conexao = conexaosql()
    cursor = conexao.cursor()


    comando  = """
            delete from conhecimentos 
            where id_conhecimento = %s
    """

    valores =(id_conhecimento,)
    cursor.execute(comando, valores)
    conexao.commit()
    if cursor.rowcount == 0:
        input("\nNenhum conhecimento encontrado com o ID especificado.")
    else:
        input("\nAs informações foram deletadas com sucesso!")
    cursor.close()
    conexao.close()