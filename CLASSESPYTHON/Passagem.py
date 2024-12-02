class Passagem:
    def __init__(self,Preco,Assento):
        self.Preco = Preco
        self.Assento = Assento

    def alterar_preco(self,novo_preco):
        self.Preco = novo_preco
        return self.Preco
    
    def escolher_assento(self):
        return self.Assento
    
class PassagemAviao(Passagem):
    def __init__(self,Preco,Assento,portaodeembarque,checkin):
        super().__init__(Preco, Assento)
        self.portaodeembarque = portaodeembarque
        self.checkin = checkin

    def Decolar(self):
        print("O Aviao DECOLOU !!!")

    def Abastecer(self):
        print("O Aviao precisa abastecer")


class PassagemBus(Passagem):
    def __init__(self,Preco,Assento,placa,leito):
        super().__init__(Preco, Assento)
        self.placa = placa
        self.leito = leito
        
    def Partida(self):
        print("O Busão partiou!")

    def Abastecer(self):
        print("O Busão precisa abastecer")

passagem = PassagemAviao(2000,20,3,"este é o meu assento")
print(f"O preço da passagem é : {passagem.Preco}")
print(f"O seu Assento é : {passagem.Assento}")
print(f"O seu portao de embarque é : {passagem.portaodeembarque}")
print(f"O seu checkin é {passagem.checkin}")
print(passagem.Decolar())
print(passagem.Abastecer())


passagem2 = PassagemBus(113,10,1323321,21)
print(f"O preço da sua passagem é : {passagem2.Preco}")
print(f"O seu assento é {passagem2.Assento}")
print(f"A placa do BUS é {passagem2.placa}")
print(f"O seu leito é {passagem2.leito}")
print(passagem2.Partida())
print(passagem2.Abastecer())
