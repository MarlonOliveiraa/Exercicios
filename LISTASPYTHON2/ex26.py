
valor_base_x = int(input("digite o valor da base x : "))
valor_expoente_y = int(input("digite o valor do expoente y : "))

potencia = 1 
cont = 1 
while cont <= valor_expoente_y:
    potencia *= valor_base_x
    cont += 1 

print(f"{valor_base_x} ^ {valor_expoente_y} = {potencia}")

