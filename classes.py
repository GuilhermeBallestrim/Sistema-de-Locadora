import os


class Item:
    # Construtor

    def __init__(self, codigo: int, titulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True

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
        return self.__titulo

    def getCodigo(self):
        return self.__codigo    


# ------------------------------------------------------------------------------------------


class Filme(Item):
    # Construtor

    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        Item.__init__(self, codigo, titulo)
        self.__genero = genero
        self.__duracao = duracao

# ------------------------------------------------------------------------------------------


class Jogo(Item):
    # Construtor

    def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
        Item.__init__(self, codigo, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

# ------------------------------------------------------------------------------------------


class Cliente:
    # Construtor

    def __init__(self, nome: str, cpf: int, itensLocados=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = itensLocados if itensLocados is not None else []

    # Métodos

    def locar(self, item: Item):
        if item not in self.__itensLocados:
            item.alugar()
            self.__itensLocados.append(item)
        else:
            print("Este item já está locado por um cliente.")

    def devolver(self, item: Item):
        if item in self.__itensLocados:
            item.devolver()
            self.__itensLocados.remove(item)
        else:
            print("Este item não está locado.")

    def listarLocados(self):
        if self.__itensLocados:
            print(f"Itens locados por {self.__nome} - {self.__cpf}:")
            for item in self.__itensLocados:
                print(f"- [{item.getCodigo()}] {item.getTitulo()}")
        else:
            print(f"{self.__nome} não possui itens locados.")
    
    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf


# ------------------------------------------------------------------------------------------


class Locadora:
    # Construtor

    def __init__(self, clientes=None, itens=None):
        self.__clientes = clientes if clientes is not None else []
        self.__itens = itens if itens is not None else []

    # Métodos

    def cadastrarCliente(self, cliente: Cliente):
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)
            print(f"Cliente {cliente.getNome()} adicionado com sucesso.")
        else:
            print(f"Cliente {cliente.getNome()} já está cadastrado.")

    def cadastrarItem(self, item: Item):
        if item not in self.__itens:
            self.__itens.append(item)
            print(f"Item '{item.getTitulo()}' adicionado com sucesso.")
        else:
            print(f"Item '{item.getTitulo()}' já está cadastrado.")

    def listarClientes(self):
        if self.__clientes:
            print("Clientes Cadastrados:")
            for item in self.__clientes:
                print(f"| {Cliente.getNome()} -- {Cliente.getCpf()} ")
        else:
            print("Nenhum cliente cadastrado na locadora.")

    def listarItens(self):
        if self.__itens:
            print("Itens Cadastrados:")
            for item in self.__itens:
                print(f"| {Item.getCodigo()} -- {Item.getTitulo()} ")
        else:
            print("Nenhum título cadastrado na locadora.")
    
    
