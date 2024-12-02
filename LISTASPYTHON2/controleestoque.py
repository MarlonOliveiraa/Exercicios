codigos = []
descricoes = []
quantidades = []

print("CONTROLE DE ESTOQUE")

def adicionar_produto(codigo, descricao, quantidade):
    codigos.append(codigo)
    descricoes.append(descricao)
    quantidades.append(quantidade)
    print("Produto adicionado com sucesso!")

def remover_produto(codigo):
    if codigo in codigos:
        index = codigos.index(codigo)
        del codigos[index]
        del descricoes[index]
        del quantidades[index]
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado")
 

def atualizar_quantidade(codigo, nova_quantidade):
    if codigo in codigos:
        index = codigos.index(codigo)
        quantidades[index] = nova_quantidade
        print("Quantidade atualizada com sucesso!")
    else:      
        print("Produto não encontrado")

def mostrar_estoque():
    print("Estoque:")
    for i in range(len(codigos)):
        print("Código:", codigos[i])
        print("Descrição:", descricoes[i])
        print("Quantidade:", quantidades[i])
        print("--------------------")

# Exemplo da utilização das funções
adicionar_produto("001", "Smartphone", 50)
adicionar_produto("002", "Tablet", 30)
mostrar_estoque()
remover_produto("002")
atualizar_quantidade("001", 40)
mostrar_estoque()