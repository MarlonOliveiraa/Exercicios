class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome 
        self.autor = autor 
        self.editora = editora 
        self.paginas = paginas

    def Alterar_editora(self,nova_editora):
       
       self.editora = nova_editora
       return self.editora

    def Listar_qtde_paginas(self):
        return self.paginas 

livro1 = Livro("the code","marlon","darkside",100)
print(livro1.editora)
print(livro1.Alterar_editora("recort"))
print(livro1.editora)