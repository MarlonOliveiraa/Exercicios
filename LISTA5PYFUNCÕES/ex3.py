def verificanegativopositivo(numero):
    if numero > 0:
        return "1"
    elif numero == 0:
        return "0"
    else:
        return "-1"
    
entrada_usuario = float(input("digite um número: "))
resultado = verificanegativopositivo(entrada_usuario)
print(f"o resultado é : {resultado}")

