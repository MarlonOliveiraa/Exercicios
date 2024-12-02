idades = []
media = 0 
 
while True:
    idade = int(input("Digite algumas idades  (0 para sair): "))
    idades.append(idade)
    if idade  == 0:
        break
idades.pop()
media = sum(idades) / len(idades)

print("A idade media desse grupo é:",media)
