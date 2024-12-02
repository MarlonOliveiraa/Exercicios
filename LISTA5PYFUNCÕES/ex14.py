def calculo_de_consumo(distancia_km,litros):
    consumo = distancia_km / litros 
    if consumo < 8:
        return f"Gasta muito!"
    elif 8 <= consumo <= 15:
        return f"Econômico!"
    else:
        return f"Super econômico!"
    
distancia_km = 100 
litros = 5
mensagem = calculo_de_consumo(distancia_km,litros)
print(mensagem)
