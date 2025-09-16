from classes import *
import os
import time

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
        print("Bem vindo ao Sistema de Aluguéis da >> Checkpoint Locadora <<")
        esperarTela()
        print("Opções:")
        print("  1 - Locar Item             |  5 - Cadastrar Item \n  2 - Devolver Item          |  6 - Listar Clientes Cadastrados \n  3 - Listar Itens Locados   |  7 - Listar Itens Cadastrados\n  4 - Cadastrar Cliente      |  0 - Sair")
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
                    pularLinha()
                    esperarTela()
                    print("Valor inválido, insira apenas números")
                    pularLinha()
                    pausarTela()
                    continue
                novo_cliente = Cliente(nome=nome, cpf=cpf)
                esperarTela()
                locadora.cadastrarCliente(novo_cliente)
                esperarTela()
                pularLinha()
                esperarTela()
            
            case "5":
                limparTela()
                print(f"Você escolheu a opção: 5 - Cadastrar Item")
                esperarTela()
                print("Insira o título do novo item:")
                titulo=input("--> ")
                print("Insira o código do novo item (apenas números)")
                try:
                    codigo=input("--> ")
                    int(codigo)
                except ValueError:
                    pularLinha()
                    esperarTela()
                    print("Valor inválido, insira apenas números")
                    pularLinha()
                    pausarTela()
                    continue
                esperarTela()
                limparTela()
                chF=input(f"Insira a categoria do Item: '{titulo}'\n1 - Filme\n2 - Jogo\n--> ")
                esperarTela()
                limparTela()
                match chF:
                    case '1':
                        genero=input("Insira o gênero do novo filme\n--> ")
                        esperarTela()
                        try:
                            duracao=(input("Insira a duração (em minutos) do novo filme (apenas números)\n--> "))
                            esperarTela()
                            int(duracao)
                        except ValueError:
                            pularLinha()
                            esperarTela()
                            print("Valor inválido, insira apenas números")
                            pularLinha()
                            pausarTela()
                            continue
                        novo_item=Filme(codigo=codigo, titulo=titulo, genero=genero, duracao=duracao)
                        esperarTela()
                        locadora.cadastrarItem(novo_item)
                        esperarTela()
                        pularLinha()
                        esperarTela()
                    case '2':
                        plataforma=input("Insira a plataforma do novo jogo\n--> ")
                        esperarTela()
                        try:
                            faixaEtaria=(input("Insira a faixa etária do novo jogo (apenas números)\n--> "))
                            esperarTela()
                            int(faixaEtaria)
                        except ValueError:
                            pularLinha()
                            esperarTela()
                            print("Valor inválido, insira apenas números")
                            pularLinha()
                            pausarTela()
                            continue
                        novo_item=Jogo(codigo=codigo, titulo=titulo, plataforma=plataforma, faixaEtaria=faixaEtaria)
                        esperarTela()
                        locadora.cadastrarItem(novo_item)
                        esperarTela()
                        pularLinha()
                        esperarTela()
                    case _:
                        print("Opção inválida, tente novamente...")
                        esperarTela()
                        pularLinha()
                        pausarTela()
                        
            
            case "6":
                print(f"Você escolheu a opção: 6 - Listar Clientes Cadastrados")
                pularLinha()
                esperarTela()
                locadora.listarClientes()
                esperarTela()
            
            case "7":
                print(f"Você escolheu a opção: 7 - Listar Itens Cadastrados")
                pularLinha()
                esperarTela()
                locadora.listarItens()
                esperarTela()
                pausarTela()
            
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