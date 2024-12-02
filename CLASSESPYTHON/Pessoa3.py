class Pessoa3:
    def __init__(self,nome,telefone,email,endereco):
        self.nome = nome 
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def negociar(self):
        print("VAMOS NEGOCIAR")

class PessoaFisica(Pessoa3):
    def __init__(self, nome, telefone, email, endereco,cpf = float):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def negociar(self):
        print("VAMOS NEGOCIAR")

    def estudar(self):
        return "ESTOU ESTUDANDO"
    
    def mostrarCPF(self):
        return self.cpf
    
class PessoaJuridica(Pessoa3):
    def __init__(self, nome, telefone,email,endereco,cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def negociar(self):
        return "VAMOS NEGOCIAR"

    def mostrarCNPJ(self):
        return self.cnpj
    
    def DeclarImposto(self):
        return "PRECISO DECLARAR MEU IMPOSTO SE NÃO A POLICIA ME PEGA!"

pessoa = PessoaFisica("Marlon Oliveira",656445445,"marlonsantana@gmail.com","rua goiaba 235","254.365.981.45",)
print(f"O nome da pessoa é : {pessoa.nome}")
print(f"O telefone da pessoa é : {pessoa.telefone}")
print(f"O email da pessoa é : {pessoa.email}")
print(f"O endereço da pessoa é :{pessoa.endereco}")
print(f"O CPF da pesoa é {pessoa.cpf}") 

print(pessoa.negociar()) 
print(pessoa.estudar()) 
print(pessoa.mostrarCPF()) 


pessoa1 = PessoaJuridica("Marlon Oliveira",656445445,"marlonsantana@gmail.com","rua goiaba 235","254.365.981.45",)
print(f"O nome da pessoa é : {pessoa1.nome}")
print(f"O telefone da pessoa é : {pessoa1.telefone}")
print(f"O email da pessoa é : {pessoa1.email}")
print(f"O endereço da pessoa é :{pessoa1.endereco}")
print(f"O CNPJ da pesoa é {pessoa1.cnpj}") 

print(pessoa1.negociar())
print(pessoa1.mostrarCNPJ())
print(pessoa1.DeclarImposto())

