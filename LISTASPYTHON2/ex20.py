numeros = []
pares = 0
 
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    if numero == 0:
        break
    numero.append(numero)
    if numero % 2 == 0:
        pares += 1
 
print("Número de dados lidos:", len(numeros))
print("Número de valores pares:", pares)