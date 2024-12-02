def calcular_media(nota1, nota2, nota3, letra):
    notas = [nota1, nota2, nota3]
    if letra == 'A':
     
        media = sum(notas) / len(notas)
    elif letra == 'P':
      
        pesos = [5, 3, 2]
        
        media = sum(nota * peso for nota, peso in zip(notas, pesos)) / sum(pesos)
    else:
        raise ValueError("Letra inválida. Use 'A' para média aritmética ou 'P' para média ponderada.")
    return media


nota1 = 7  # exemplo de nota 1
nota2 = 8  # exemplo de nota 2
nota3 = 9  # exemplo de nota 3
letra_indicadora = 'A'  # exemplo de letra indicadora para média aritmética

# Calcular a média
media = calcular_media(nota1, nota2, nota3, letra_indicadora)

# Imprimir o resultado
print(f"A média do aluno com as notas {nota1}, {nota2}, {nota3} e letra indicadora '{letra_indicadora}' é {media:.2f}.")
