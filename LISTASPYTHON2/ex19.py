num = int(input("digite um numero entre 100 e 9999: "))

if 100 <= num <= 9999:
    print("NUMERO VALIDO")
palavra = (num)
i = 0
for numero in palavra:
    print(f'Posição {i} Letra: {num}')
    i += 1
else:
    print("NUMERO INVALIDO  ")