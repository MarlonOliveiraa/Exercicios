
class Filme:
    def __init__(self,nome,duração):
        self.nome = nome
        self.duração = duração

    def Play(self):
        print(f"O filme {self.nome} foi dado play")

class Acao(Filme):
    def __init__(self,nome,duração,ano):
        super().__init__(nome,duração)
        self.ano = ano

    def explodir(self):
        return f"KABUMMM"

class Romance(Filme):
    def __init__(self, nome, duração,personagem):
        super().__init__(nome, duração)
        self.personagem = personagem



filme = Acao("AS AVENTURAS DE KABUMMM","1:50",2024)
print(filme.nome)
print(filme.explodir())
         

