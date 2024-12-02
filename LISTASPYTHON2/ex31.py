salario = 4000
aumento = 0.015

for ano in range (2020,2024):
    salario += salario * aumento 
    aumento *= 2

print(f"o salario atual do funcionario é {salario}")

