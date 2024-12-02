def soma_inteiros(n1,n2):
    soma = 0
    for numero in range(n1, n2 + 1 ):
        if isinstance(numero, int):
            soma += numero
    return numero

resultado = soma_inteiros(1,10)
print(f"A soma dos numeros inteiros entre 1 e 10:{resultado}")