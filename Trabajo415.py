# Pedimos al usuario el número de asteriscos por lado
numero_asteriscos = int(input("Introduce el número de asteriscos por lado: "))

# Bucle for anidado para imprimir el cuadrado
for fila in range(numero_asteriscos):
    # Imprimimos la primera columna de asteriscos
    if fila == 0 or fila == numero_asteriscos - 1:
        print("* " * numero_asteriscos)
    else:
        # Imprimimos el primer asterisco
        print("*", end="")
        
        # Imprimimos espacios en blanco en el centro
        for espacio in range(numero_asteriscos - 2):
            print(" ", end=" ")
        
        # Imprimimos el último asterisco
        print(" *")