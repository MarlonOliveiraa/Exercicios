class Triangulo:
    def __init__(self,lado_A,lado_B,lado_C):
        self.lado_A = lado_A
        self.lado_B = lado_B
        self.lado_C = lado_C
        
    def calcular_perimetro(self):
        
        self.lado_A = int(input("DIGITE O VALOR DO LADO A: "))
        self.lado_B = int(input("DIGITE O VALOR DO LADO B: "))
        self.lado_C = int(input("DIGITE O VALOR DO LADO C: "))
       
        return self.lado_A * self.lado_B * self.lado_C
 
    

    
    

         

        