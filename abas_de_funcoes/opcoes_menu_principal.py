from abas_de_funcoes.logo import logositema
from abas_de_funcoes.adicionar_conhecimento import adicionar_conhecimento
from abas_de_funcoes.lista_conhecimento import ver_lista_conhecimento
from abas_de_funcoes.remover_conhecimento import remover_conhecimento
from abas_de_funcoes.editar_conhecimento import editar_conhecimento

from colorama import init, Fore, Back
import os

init()

def menuprincipal():
    #mostrar tudo que deve ser exibido no menu principal
    os.system('cls')
    def exibir_menu_principal():
        logositema()
        opcoes_menu_principal()
        selecionar_opcao()

    return exibir_menu_principal()
 


    
def selecionar_opcao():
    """
    Função direciona o cliente para qual opção do  menu principal ele escolher
    """
    sair_do_app = False

    while not sair_do_app:
        try:
            opcao_escolhida = int(input("Escolha uma opção: "))
            match opcao_escolhida: 
                case 1:
                    adicionar_conhecimento()
                    break
                case 2:
                    editar_conhecimento()
                case 3:
                    remover_conhecimento()
                case 4:
                    ver_lista_conhecimento()
                    break
                case 5:
                    sair_do_app = finalizar_app()
                case _:
                    opcao_invalida()
        except:
            opcao_invalida()
        finally:
            if opcao_escolhida != 5:
                menuprincipal()
            else:
                break
# Fore.RED+
#     + Fore.RESET.GREEN

def opcoes_menu_principal():
    print("    |    [1] ADICIONAR NOVO CONHECIMENTO       |")
    print("    |    [2] EDITAR CONHECIMENTO               |")
    print("    |    [3] REMOVER CONHECIMENTO              |")
    print("    |    [4] VISUALIZAR LISTA DE CONHECIMENTO  |")
    print("    |    [5] SAIR DO APP                       |\n")
    

def finalizar_app():
    os.system('cls')
    logositema()
    print('\nFinalizando app :) .....\n')
    
    


def opcao_invalida():
    print('\n[ERRO] Opção inválida\n')


