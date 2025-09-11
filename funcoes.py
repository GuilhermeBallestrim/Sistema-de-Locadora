from classes import *
import os
import time
from cadastroteste import *

locadora = Locadora()

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
                limparTela()
                print(f"Você escolheu a opção: 4 - Cadastrar Cliente")
                esperarTela()
                print("Insira o nome do novo cliente:")
                nome=input("--> ")
                print("Insira o CPF do novo cliente")
                try:
                    cpf=input("--> ")
                    int(cpf)
                except ValueError:
                    print("Valor inválido, insira apenas números")
                novo_cliente = Cliente(nome=nome, cpf=cpf)
                esperarTela()
                locadora.cadastrarCliente(novo_cliente)
                esperarTela()
                pularLinha()
                esperarTela()
            
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