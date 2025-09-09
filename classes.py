class Item:
    #Construtor
    
    def __init__(self, codigo: int, titulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True
        
    #Métodos
    
    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"Item {self.__disponivel} foi alugado com sucesso.")
        else:
            print(f"Item {self.__disponivel} não está disponível.")
            
    def devolver(self):
        self.__disponivel = True
        print(f"Item {self.__disponivel} foi devolvido com sucesso.")
        
# ------------------------------------------------------------------------------------------

class Filme(Item):
    #Construtor
    
    def __init__(self, codigo: int, titulo: str, genero: str, duracao: int):
        Item.__init__(self, codigo, titulo)
        self.__genero = genero
        self.__duracao = duracao

# ------------------------------------------------------------------------------------------

class Jogo(Item):
    #Construtor
    
    def __init__(self, codigo: int, titulo: str, plataforma: str, faixaEtaria: int):
        Item.__init__(self, codigo, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria
        
# ------------------------------------------------------------------------------------------

class Cliente:
    #Construtor
    
    def __init__(self, nome: str, cpf: int, itensLocados=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = itensLocados if itensLocados is not None else []
        
    #Métodos    
    
    def locar(item: Item):
        Item.alugar()
    
    def devolver(item: Item):
        Item.devolver()