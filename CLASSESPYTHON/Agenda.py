class Agenda:
    def __init__(self,dia,mes,ano,anotacao):
        self.dia = dia
        self.mes = mes 
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        return (self.dia + self.mes + self.ano)
    
    def anotar_tarefa(self):
        return self.anotar_tarefa
    
    def Mostrar_anotacao(self):
        return self.anotacao
    
agenda = Agenda(10,08,2024,"O dia está lindo!!!")
print(agenda.validar_data())
print(agenda.anotar_tarefa())
print(agenda.Mostrar_anotacao())