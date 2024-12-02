import math

class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def imprimir_valor_raio(self):
        return self.raio
    
    def calcular_area_circulo(self):
        return math.pi * self.raio
    
    def circunferencia(self):
        return math.pi * 2 / (self.raio)
    
medidas = Circulo(20)
print(medidas.imprimir_valor_raio())
print(medidas.calcular_area_circulo())
print(medidas.circunferencia())

    

    