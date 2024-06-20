def mezclar_colores():
    print("rojo, amarillo, azul")
    
    color1 = input("primer color ")

    color2 = input("segundo color ")

    if (color1 == 'rojo' and color2 == 'azul') or (color1 == 'azul' and color2 == 'rojo'):
        print("Morado")

    elif (color1 == 'amarillo' and color2 == 'azul') or (color1 == 'azul' and color2 == 'amarillo'):
        print("verde.")

    elif (color1 == 'rojo' and color2 == 'amarillo') or (color1 == 'amarillo' and color2 == 'rojo'):
        print("Naranjado.")

    else:
        print("No son los colores a elegir")
mezclar_colores()
