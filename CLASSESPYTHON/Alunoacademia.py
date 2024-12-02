class Aluno:
    def __init__(self,nome,idade,peso,altura,valor_mensalidade = "120,00"):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.valor_mensalidade = valor_mensalidade

    def Calcular_IMC(self):
        return self.peso / self.altura ** 2
    
    def Obter_valor_menssalidade(self):
        if self.idade < 18:
            return "VC TEM O DIREITO AO DESCONTO ESPECIAL"

        else:
            return f"VC NÃO DIREITO AO DESCONTO ESPECIAL PAGARÁ MENSALIDADE DE :{self.valor_mensalidade}"    
        
aluno = Aluno("")        