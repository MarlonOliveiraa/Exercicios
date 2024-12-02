def pot(base, expoente ):
    for i in range( 1 + expoente):
        resultado = base ** i
        print(f"a {base} ** {expoente} = {resultado}")

pot(2,3)