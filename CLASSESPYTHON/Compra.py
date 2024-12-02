class Compra:
    def __init__(self,numero,produto,valor_total = 0):
        self.numero = numero
        self.produto = produto
        self.valor_total = valor_total

    def calcular_valor_total(self):
        frete = self.valor_total * 0.05
        self.valor_total + (0,17 * 100) + frete

class Avista(Compra):
    def __init__(self, numero, produto,desconto = float, valor_total=0):
        super().__init__(numero, produto, valor_total)
        self.desconto = desconto

    def Desconto(self,):
        self.valor_total - self.desconto 
        return self.valor_total
    
class Parcela(Compra):
    def __init__(self, numero, produto, valor_total= 0,numero_de_parcelas = 0):
        super().__init__(numero, produto, valor_total)
        self.numero_de_parcelas = numero_de_parcelas

    def valor_parcela(self):
        parcela = self.valor_total / self.numero_de_parcelas
        return parcela

avista = Avista("010204","celular",1000)
print(avista.produto)
print(avista.Desconto())