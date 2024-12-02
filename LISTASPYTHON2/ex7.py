notas = []
    
i = 0
for i in range (10):
    i += 1
    notas.append(int(input("digite a nota ")))
media = sum (notas) / len(notas)
print(media)
