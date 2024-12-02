class Brinquedos:
    def __init__(self,nome,cor,tamanho,preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        return f"estou brincando com {self.nome}"
    
class Aviaozinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,aviao_madeira):
        super().__init__(nome, cor, tamanho, preco)
        self.aviao_madeira = aviao_madeira

    def voar(self):
        return f"O aviao {self.nome} decoulou!"
    
class Bola(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,marca):
        super().__init__(nome, cor, tamanho, preco)
        self.marca = marca

    def chutar(self):
        return f"chuta a bola {self.nome}"

class Baralho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,quant_cartas):
        super().__init__(nome, cor, tamanho, preco)
        self.quant_cartas = quant_cartas

    def Truco(self):
        return "TRUCO SAFADO"

class Dama(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,captura):
        super().__init__(nome, cor, tamanho, preco)
        self.captura = captura 

    def Virar_dama(self):
        return "Promova uma peça a Dama"
    
class xadrez(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,versatilidade):
        super().__init__(nome, cor, tamanho, preco)
        self.versatilidade = versatilidade

    def xeque_mate(self):
        return "DEI XEQUE MATE"
    
class Pipa(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,rabiola):
        super().__init__(nome, cor, tamanho, preco)
        self.rabiola = rabiola

    def empinar(self):
        return "empinar a pipa"
    
class Domino(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,pecas):
        super().__init__(nome, cor, tamanho, preco)
        self.pecas = pecas

    def jogar(self):
        return "VAMOS JOGAR DOMINÓ"
    
class Carrinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,roda):
        super().__init__(nome, cor, tamanho, preco)
        self.roda = roda

    def correr(self):
        return "Correr com o carrinho"
    
class Boneco(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,cabeça):
        super().__init__(nome, cor, tamanho, preco)
        self.cabeça = cabeça

    def falar(self):
        return "APERTE NA BARRIGA PARA O BONECO FALAR"
    
class Skate(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,lixa):
        super().__init__(nome, cor, tamanho, preco)
        self.lixa = lixa

    def manobra(self):
        return "MANDAR UM FLIP 360"
    
skate1 = Skate("kourt koben","preto",50,400,"omo")
print(f"O nome do skate é :{skate1.nome}")
print(skate1.manobra())
