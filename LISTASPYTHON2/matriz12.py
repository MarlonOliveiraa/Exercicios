m = [[1,120, -3],[4,5,250],[7,0,9]]
l = 0
cl = 0
maior_valor = [0][0]
menor_valor = [0][0]

for linha in m :

    for elemento in linha :

        if elemento > maior_valor:
            maior_valor = elemento
        if elemento < menor_valor:
            menor_valor = elemento

print(f"O valor maximo da na matriz é :{maior_valor}")
print(f"O menor valor minimo na matriz é: {menor_valor}")

