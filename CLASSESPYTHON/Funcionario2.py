class Funcionario2:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def Bater_ponto(self):
        return "bater ponto"

class vendedor(Funcionario2):
    def __init__(self, nome, matricula, salario,comissao,vendas):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
        self.vendas = vendas

    def bater_meta(self):
        if self.vendas > 50:
            return f"PARARBÉNS VC GANHOU COMISSÃO DE : {self.comissao}"
        else:
            return "VENDE MAIS VC, NÃO GANHOU NADA DE COMISSÃO !"   


class gerente(Funcionario2):
    def __init__(self, nome, matricula, salario,senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def demitir_func(self):
        return f"VC TEM QUE DEMITIR O FUNCIONARIO {vendedor.nome}"
    
    def Mostar_senha(self):
        return self.senha
    
vendedor1 = vendedor("MARLON",23405,20000,1000,60)
print(f"O nome do vendedor é : {vendedor1.nome}")
print(f"A matricula do vendedor é : {vendedor1.matricula}")
print(f"O salario do vendedor é : {vendedor1.salario}")
print(f"A comissao do vendedor é : {vendedor1.comissao}")
print(f"Ele vendeu : {vendedor1.vendas}")

print(vendedor1.bater_meta())

gerente1 = gerente("MARLON2",24501,30000,123)
print(f"O nome do gerente é : {gerente1.nome}")
print(f"A matricula do vendedor é : {gerente1.matricula}")
print(f"O salario do vendedor é : {gerente1.salario}")
print(f"A senha do vendedor é : {gerente1.senha}")

print(gerente1.demitir_func())
print(gerente1.Mostar_senha())



    