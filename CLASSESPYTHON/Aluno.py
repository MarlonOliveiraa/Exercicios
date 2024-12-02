class Aluno:
    def __init__(self,nome,RA,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.RA = RA
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def Media_aritmedica(self,):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
    
    def Mostrar_situacao(self):
        media = self.Media_aritmedica()
        if media >= 7:
            return "APROVADO"
        elif 5 <= media < 6.9:
            return "EXAME"
        else:
            return "REPROVADO"
        

aluno = Aluno("Marlon",123456,10,10,6,6)
print(f"O nome do Aluno é: {aluno.nome}")
print(f"A RA do Aluno é: {aluno.RA}")
print(f"A situação do aluno é: {aluno.Mostrar_situacao()}")



        

        
        
        
        

        