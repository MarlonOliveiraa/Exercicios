import math

def volume_cilindro(altura,raio):
    volume = math.pi * raio ** 2 * altura
    return volume

if __name__ == "__main__":
    raio_teste = 5 
    volume = volume_cilindro(raio_teste) 
    print(f"O volume de uma esfera com raio {raio_teste} é {volume:.2f}")

