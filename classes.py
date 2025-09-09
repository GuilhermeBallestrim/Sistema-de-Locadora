class Item:
    #Construtor
    
    def __init__ (self, codigo, titulo, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = disponivel
        
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