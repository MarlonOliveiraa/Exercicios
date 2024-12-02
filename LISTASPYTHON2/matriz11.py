m = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

soma = 0 
mat = []
for linha in range(3):
    for coluna in range(3):
       if linha == coluna:
           soma = soma + mat[linha][coluna]

print(soma)
    
