class Pessoa2:
    def __init__(self,Matricula,Nome,Idade):
        self.Matricula = Matricula
        self.Nome = Nome
        self.Idade = Idade

class Professor(Pessoa2):
    def __init__(self,Formacao,disciplina,carga_horaria,salario):
        self.Formacao = Formacao 
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria 
        self.salario = salario


class Aluno(Pessoa2):
    def __init__(self, Matricula, Nome, Idade,notas
                 ):
        super().__init__(Matricula, Nome, Idade)


 
    
    