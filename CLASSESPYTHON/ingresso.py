class Ingresso:
    def __init__(self,Preco,Setor):
        self.Preco = Preco
        self.Setor = Setor

    def alterar_Preco(self,novo_preco):
        self.Preco = novo_preco
        return self.Preco
    
    def mostrar_setor(self):
        return self.Setor
    
class IngressoVIP(Ingresso):
    def __init__(self, Preco, Setor,camarote,open_bar,open_food,estacionamento):
        super().__init__(Preco, Setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def Pegar_bebida(self):
        return self.open_bar
    
    def acessar_camarote(self):
        return self.camarote
    
ingresso = IngressoVIP(100,2,10,"SKOL","PEIXE FRITO,","3HRS")
print(ingresso.alterar_Preco(300))
print(ingresso.mostrar_setor())
print(ingresso.Pegar_bebida())
print(ingresso.acessar_camarote())