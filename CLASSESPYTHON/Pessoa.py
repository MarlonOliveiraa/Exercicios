class Pessoa:
    def __init__(self,nome,idade,Endereço):
        self.nome = nome
        self.idade = idade 
        self.Endereço = Endereço

    def mostrar_nome(self):
        return self.nome
    
    def alterarIdade(self):
        return self.idade
    
    def imprimirEndereço(self):
        return self.Endereço

pessoa1 = Pessoa("Gisele",18,"UNIAO")
pessoa2 = Pessoa("Marlon",23,"TIJUCA")


print(f"O nome da pessoa é {pessoa1.nome} ,ela tem {pessoa1.idade} anos e mora no {pessoa1.Endereço} ")
print(f"O nome da pessoa é {pessoa2.nome} ,ele tem {pessoa2.idade} anos e mora no {pessoa2.Endereço} ")