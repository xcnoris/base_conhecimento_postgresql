
from conexao_postgresql.conexao_sql import conexaosql
from abas_de_funcoes.exibir_subtitulo import exibir_subtitulo
from abas_de_funcoes.listadeconhecimentos import listadeconhecimentos

import datetime

def adicionar_conhecimento():
     while True:
        exibir_subtitulo('Adicionar novo conhecimento')
        
        
        
        listadeconhecimentos()
        id_categoria = 5 + int(input("Digite o id da categoria do conhecimento: "))
        titulo = input("Digite o título do conhecimento: ")
        descricao = input("Digite a descricao do conhecimento: ")
        id_usuario = input("Digite o id do usuario que esta criando esse conhecimento: ")
        data_criacao = datetime.datetime.now()

        conexao = conexaosql()
        cursor = conexao.cursor()
            
        comando = """
            INSERT INTO conhecimentos (id_categoria, titulo, descricao, id_usuario, data_criacao) VALUES
        (%s, %s, %s, %s, %s)
        """    
        valores = (id_categoria, titulo, descricao, id_usuario, data_criacao)
        cursor.execute(comando, valores)
        conexao.commit()
        print("As informações foram salvas com sucesso!")
        cursor.close()
        conexao.close()
        
        opcao = input("Deseja adicionar mais um conhecimento? (s/n): ")
        if opcao.lower() != 's':
            return False
        return True


