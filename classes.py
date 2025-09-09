import os


class Item:
    # Construtor

    def __init__(self, codigo: int, titulo: str):
        try:
            self.__codigo = codigo
            self.__titulo = titulo
            self.__disponivel = True
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    # Métodos

    def alugar(self):
        try:
            if self.__disponivel:
                self.__disponivel = False
                print(f"Item '{self.__titulo}' foi alugado com sucesso.")
            else:
                print(f"Item {self.__titulo} não está disponível.")
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    def devolver(self):
        try:
            if not self.__disponivel:
                self.__disponivel = True
                print(f"Item '{self.__titulo}' foi devolvido com sucesso.")
            else:
                print("Este item não está locado")
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    def getTitulo(self):
        try:
            return self.__titulo
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    def getCodigo(self):
        try:
            return self.__codigo
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")


# ------------------------------------------------------------------------------------------


class Filme(Item):
    # Construtor

    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        try:
            Item.__init__(self, codigo, titulo)
            self.__genero = genero
            self.__duracao = duracao
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")


# ------------------------------------------------------------------------------------------


class Jogo(Item):
    # Construtor

    def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
        try:
            Item.__init__(self, codigo, titulo)
            self.__plataforma = plataforma
            self.__faixaEtaria = faixaEtaria
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")


# ------------------------------------------------------------------------------------------


class Cliente:
    # Construtor

    def __init__(self, nome: str, cpf: int, itensLocados=None):
        try:
            self.__nome = nome
            self.__cpf = cpf
            self.__itensLocados = itensLocados if itensLocados is not None else []
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    # Métodos

    def locar(self, item: Item):
        try:
            if item not in self.__itensLocados:
                item.alugar()
                self.__itensLocados.append(item)
            else:
                print("Este item já está locado por um cliente.")
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    def devolver(self, item: Item):
        try:
            if item in self.__itensLocados:
                item.devolver()
                self.__itensLocados.remove(item)
            else:
                print("Este item não está locado.")
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")

    def listarItens(self):
        try:
            if self.__itensLocados:
                print(f"Itens locados por {self.__nome}:")
                for item in self.__itensLocados:
                    print(f"- [{item.getCodigo()}] {item.getTitulo()}")
            else:
                print(f"{self.__nome} não possui itens locados.")
        except Exception as e:
            print(f"Ocorreu um erro Inesperado: {e}")
            os.system("pause")