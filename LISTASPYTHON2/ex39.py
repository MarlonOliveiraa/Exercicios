a = int(input("digite os numeros de a : "))
b = int(input("digite os numeros de b : "))
i = 0  

for divisor in range(2,a):
    if a % divisor == 0:
        print(f"{divisor} não é primo !")
        break
    else:
        print(f"{divisor} é primo ! ")
   