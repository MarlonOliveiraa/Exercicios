def calcular_consumo(distancia_km, litros_gasolina):
    # Calcula o consumo em km/l
    consumo = distancia_km / litros_gasolina
    
    # Mensagem de acordo com a eficiência
    if consumo < 8:
        return f"Consumo: {consumo:.2f} km/l - Venda o carro!"
    elif 8 <= consumo < 12:
        return f"Consumo: {consumo:.2f} km/l - Econômico!"
    else:
        return f"Consumo: {consumo:.2f} km/l - Super econômico!"

# Exemplo de uso da função
distancia = 100  # km
litros = 5      # litros de gasolina

# Chama a função e imprime o resultado
mensagem = calcular_consumo(distancia, litros)
print(mensagem)

