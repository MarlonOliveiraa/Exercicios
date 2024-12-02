class Funcionário:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nomeCompleto(self):
        return self.nome + self.sobrenome
            
    def calcularSalario(self):
            return self.horas_trabalhadas * self.valor_hora
        
    def incrementarHoras(self,horas_add):
            return self.horas_trabalhadas + horas_add
        
funcionario = Funcionário("Marlon","Oliveira",20,6)
print(f"O nome do funcionário é:{funcionario.nome}")
print(f"O sobrenome é: {funcionario.sobrenome}")
print(f"Trabalhou {funcionario.horas_trabalhadas} horas")
print(f"O valor da sua hora é {funcionario.valor_hora}")

print(funcionario.nomeCompleto())
print(funcionario.calcularSalario())
print(funcionario.incrementarHoras())


            
        

        
        