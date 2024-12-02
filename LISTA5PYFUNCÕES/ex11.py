def calcular(n1,n2,simbolo):
    if simbolo == "+":
        return n1 + n2 
    elif simbolo == "-":
        return n1 - n2
    elif simbolo == "/":
        return n1 / n2
    elif simbolo == "*":
        return n1 * n2
    else:
        return "OPERAÇÃO INVALIDA"
    
num1 = 10
num2 = 5
simbolo = '+'
resultado = calcular(num1, num2, simbolo)
print(f"O resultado da operação {num1} {simbolo} {num2} é {resultado}")