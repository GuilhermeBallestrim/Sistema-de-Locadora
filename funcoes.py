from classes import *
import os
import time
from cadastroteste import *

def limparTela():
    os.system('cls')
    
def pausarTela():
    os.system('pause')

def esperarTela():
    time.sleep(1.0)
    
def pularLinha():
    print('')

def main():
    while True:
        limparTela()
        print("Bem vindo ao Sistema de Aluguéis da Checkpoint Locadora")
        esperarTela()
        print("Opções:")
        print("1 - Locar Item            |  2 - Devolver Item\n3 - Listar Itens Locados  |  4 - Cadastrar Cliente\n5 - Cadastrar Item        |  6 - Listar Clientes\n7 - Listar Itens          |  0 - Sair")
        ch = input("\n")

        pularLinha()
        pausarTela()
        limparTela()
        pularLinha()
        match ch:
            case "1":
                pass
            
            case "2":
                pass
            
            case "3":
                pass
            
            case "4":
                pass
            
            case "5":
                pass
            
            case "6":
                pass
            
            case "7":
                pass
            
            case "0":
                print(f"Você escolheu a opção: 0 - Sair")
                pularLinha()
                esperarTela()
                print("Saindo do sistema")
                esperarTela()
                print(".")
                esperarTela()
                print(".")
                esperarTela()
                print(".")
                esperarTela()
                pausarTela()
                limparTela()
                print("Até mais!...")
                pularLinha()
                break
            
            case _:
                print("Opção inválida, tente novamente...")
                esperarTela()
                pularLinha()
                pausarTela()

main()