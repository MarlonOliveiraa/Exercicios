class Gato:
    def __init__(self,nome,cor,peso):
        self.cor = cor
        self.peso = peso
        self.nome = nome

    def dormir(self):
        print(f" {self.nome} Mioouuuuu")


gato1 = Gato("Gato de Botas","Laranja",5)
gato2 = Gato("Félix ","Preto e Branco",5)

print(f"{gato2.nome} é {gato2.cor} e tem {gato2.peso} Kilos")

gato2.dormir()