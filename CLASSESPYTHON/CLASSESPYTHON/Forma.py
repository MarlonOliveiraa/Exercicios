class Forma:
    def __init__(self,nome):
        self.nome = nome
    
    def descricao(self):
        return f"FORMA:{self.nome}"
    
class Quadrado(Forma):
    def __init__(self, nome,lado = float):
        super().__init__(nome)
        self.lado = lado

    def descricao(self):
        return super().
            descricao(f"Forma:Quadrado,lado:"{self.lado})
        
            

