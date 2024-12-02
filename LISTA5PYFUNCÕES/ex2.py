def exibir_por_extenso(dia,mes,ano):
    meses_por_extenso = ["janeiro","Feveiro","Março","Abril","Maio",
                         "Junho","Julho","Agosto","Setembro","Outubro",
                         "Novembro","dezembro"]
    
    #dia = int(input("digite o dia : "))
    #mes = int(input("digite o dia : "))
    #ano = int(input("digite o dia : "))

    data_por_extenso = f"{dia} de {meses_por_extenso[mes - 1 ]} de {ano}"
    print(data_por_extenso)

exibir_por_extenso(1,1,2000)


