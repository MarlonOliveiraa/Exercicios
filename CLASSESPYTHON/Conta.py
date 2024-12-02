class Conta:
    def __init__(self,Nome,CPF = str,Numero = int,Saldo = 0.0):
        self.Nome = Nome
        self.CPF = CPF
        self.Numero = Numero
        self.saldo = Saldo

    def Depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito no valor de R$:{valor} Realizado com sucesso.")
        else:
            print(f"Valor de Deposito Inválido!")
        
    def Sacar(self,valor):
        if self.saldo > 0:
            self.saldo -= valor
            print(f"Saque no valor de R$:{valor} Realizado com sucesso.")
        else:
            print(f"Saldo negativo!!!,Tente novamente mais tarde.")  

    def Imprimir_saldo(self):
        return self.saldo
    
cliente = Conta("Manoel","456.654.654.45",679999999)
print(f"NOME: {cliente.Nome}")
print(f"CPF: {cliente.CPF}")
print(f"NUMERO: {cliente.Numero}")
print(f"SALDO: {cliente.saldo}")
cliente.Imprimir_saldo()

cliente.Depositar(100)
cliente.Imprimir_saldo

cliente.Sacar(100)
cliente.Imprimir_saldo()  

cliente.Sacar(2000)
    