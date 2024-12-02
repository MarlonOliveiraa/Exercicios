class Transporte:
    def __init__(self,__capacidade):
        self.__capacidade = __capacidade

class Terrestre(Transporte):
        def __init__(self, capacidade,numero_de_rodas,cor,numero_de_portas,placa):
             super().__init__(capacidade)
             self.numero_de_rodas = numero_de_rodas
             self.cor = cor
             self.numero_de_portas = numero_de_portas

class Aquatico(Transporte):
        def __init__(self,__capacidade,lemo,vela,ancora):
            super().__init__(__capacidade) 
            self.lemo = lemo
            self.vela = vela
            self.ancora = ancora

class Areo(Transporte):
        def __init__(self, __capacidade,flap,trem_de_bordo,turbina,tamanho):
            super().__init__(__capacidade)
            self.flap = flap
            self.trem_de_bordo = trem_de_bordo
            self.turbina = turbina
            self.tamanho = tamanho

class Lancha(Aquatico):
        def __init__(self, __capacidade,lemo, vela, ancora,velocidade):
            super().__init__(__capacidade, lemo, vela, ancora)
            self.velocidade = velocidade

        def correr(self):
              return "BORA CORRER NA LANCHA"
        
class Nacio(Aquatico):
        def __init__(self, __capacidade, /, lemo, vela, ancora,tipo_combustivel):
            super().__init__(__capacidade, lemo, vela, ancora)
            self.tipo_de_combustivel = tipo_combustivel
        
        def navegar(self):
              return "VAMOS NAVEGAR ATE A ROMA"

class Aviaomonomotor(Areo):
        def __init__(self, __capacidade, /, flap, trem_de_bordo, turbina, tamanho,modelo):
            super().__init__(__capacidade, flap, trem_de_bordo, turbina, tamanho)
            self.modelo = modelo

        def pousar(self):
              return "POUSAR EM SAN DIEGO"
        
class AviaoComercial(Areo):
        def __init__(self, __capacidade, /, flap, trem_de_bordo, turbina, tamanho,aeromocas,piloto):
            super().__init__(__capacidade, flap, trem_de_bordo, turbina, tamanho)
            self.piloto = piloto
            self.aeremocas = aeromocas

        def servico_de_bordo(self):
            return f"PRECISO DO SERVIÇO DE BORDO CHAME A AEROMOÇA {self.aeremocas}"

aviaocomercial = AviaoComercial(300,"abrir os flaps para pousar","abrir o trem de bordo","grande","tamanho comercial","Verônica, Mariana e Júlia","Tomas Shelby")
print(aviaocomercial.aeremocas)
print(aviaocomercial.servico_de_bordo)
print(aviaocomercial.piloto)
print(aviaocomercial.flap)
print(aviaocomercial.__capacidade)


terrestre = Terrestre(5,4,"preto",4,"HRJ-1267")
print(terrestre.__capacidade)
print(terrestre.numero_de_rodas)
print(terrestre.cor)
print(terrestre.numero_de_portas)