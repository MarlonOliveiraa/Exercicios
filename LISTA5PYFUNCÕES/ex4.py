def numero_em_segundos(horas,minutos,sugundos):
    return horas * 3600 + minutos * 60 + segundos

horas = 2
minutos = 30
segundos = 45

total_segundos = numero_em_segundos(horas,minutos, segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos são iguais a {total_segundos} segundos.")


