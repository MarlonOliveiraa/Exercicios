import math 

    # Define a função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * (9.0/5.0) + 32.0
    return fahrenheit

# Exemplo de uso da função
temperatura_celsius = 25.0
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} graus Celsius é igual a {temperatura_fahrenheit} graus Fahrenheit.")



