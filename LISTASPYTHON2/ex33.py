#vet1 = [5,10,20,30,50]
#vet2 = []
#i = 0
#while i < len(vet1):
 #   vet2.append(vet1[i]*5)
  #  i = i + 1

#print(vet1)
#print(vet2)
#vet1 = [2,4,6,8,10,12,14,16,18,20]
#vet2 = []
#i = 0
#while i < len(vet1):
    #vet2.append(int(input("Digite um novo valor :")))
#print(vet)

vetor = [10,11,12,13,14,16,18,20]
i = 0 
while i < 5:
    i += 1
    novo_valor = int(input("digite um novo valor : "))
    if novo_valor in vetor:
      print("este valor se encontra no vetor")
    else:
      vetor.append(novo_valor)


print(vetor)

   


    