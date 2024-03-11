from conexao_postgresql.conexao_sql import conexaosql
from abas_de_funcoes.exibir_subtitulo import exibir_subtitulo
from abas_de_funcoes.listadeconhecimentos import listadeconhecimentos
import os


def ver_lista_conhecimento():
    exibir_subtitulo('Lista de Conhecimentos')
    def listar_todos_os_conhecimentos():
        exibir_subtitulo('Lista de Conhecimentos')
        conexao = conexaosql()
        cursor = conexao.cursor()

        comando = """
                SELECT c.id_conhecimento,
                    cat.nome_categoria AS categoria,
                    c.titulo,
                    u.nome_usuario AS usuario,
                    TO_CHAR(c.data_criacao, 'DD/MM/YYYY') AS data_criacao_formatada
                FROM conhecimentos c
                JOIN categoria cat ON c.id_categoria = cat.id_categoria
                JOIN usuarios u ON c.id_usuario = u.id_usuario;
        """
        cursor.execute(comando)

        resultados = cursor.fetchall()

        if len(resultados) == 0:
            print("Nenhum conhecimento encontrado.")
        else:
            print('Lista de conhecimento completa: \n')
            print(f'{'ID'.ljust(7)} | {'Categoria'.ljust(15)} | {'Titulo'.ljust(50)} | {'Autor'.ljust(25)} | {'Data de criação'}')
            for res in resultados:
                print(f'{str(res[0]).ljust(7)} | {str(res[1]).ljust(15)} | {res[2].ljust(50)} | {str(res[3]).ljust(25)} | {res[4]}')
            print('\nDigite qualquer tecla para voltar ao menu principal: ')
                

        cursor.close()
        conexao.close()
        input('')



    def listar_conhecimentos_por_categoria():
        exibir_subtitulo('Lista de Conhecimentos')
        listadeconhecimentos()
        opcao_escolhida = 5 + int(input('Escolha uma categoria para filtrar os conhecimentos: '))
        conexao = conexaosql()
        cursor = conexao.cursor()

        comando = """
            SELECT c.id_conhecimento,
                    cat.nome_categoria AS categoria,
                    c.titulo,
                    u.nome_usuario AS usuario,
                    TO_CHAR(c.data_criacao, 'DD/MM/YYYY') AS data_criacao_formatada
                FROM conhecimentos c
                JOIN categoria cat ON c.id_categoria = cat.id_categoria
                JOIN usuarios u ON c.id_usuario = u.id_usuario
                 where c.id_categoria = %s
        """
        valores = (opcao_escolhida,)
        cursor.execute(comando, valores)
            
        # Recupere e manipule os resultados conforme necessário
        resultados = cursor.fetchall()
        #Verifica se teve algum retorno do comando
        if len(resultados) == 0:
            os.system('cls')
            exibir_subtitulo('Lista de Conhecimentos')
            print("Nenhum conhecimento encontrado!\n")
            input('Digite qualquer tecla para voltar ao menu principal: ')
        else:
            #Caso a consulta tenha retorno, ele mostrar ela formatada para o usuario
            os.system('cls')
            print('Lista de conhecimento completa: \n')
            exibir_subtitulo('Lista de Conhecimentos')
            print(f'{'ID'.ljust(7)} | {'Categoria'.ljust(15)} | {'Titulo'.ljust(50)} | {'Autor'.ljust(25)} | {'Data de criação'}')
            for res in resultados:
                print(f'{str(res[0]).ljust(7)} | {str(res[1]).ljust(15)} | {res[2].ljust(50)} | {str(res[3]).ljust(25)} | {res[4]}')
            input('\nDigite qualquer tecla para voltar ao menu principal: ')
        #Encerra a conexao com o banco
        cursor.close()
        conexao.close()
        

    print('1. Ver todos os conhecimentos')
    print('2. Ver conhecimentos por categoria\n')

    opcao_escolhida = int(input('Escolha uma opção(ou digite qualquer outrar tecla para voltar ao menu principal): '))
    #Verifica qual a opção escolhida pelo usuario
    if opcao_escolhida == 1:
        listar_todos_os_conhecimentos()
    if opcao_escolhida == 2:
        listar_conhecimentos_por_categoria()