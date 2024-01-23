def calcular_iva(valor):
    try:
        iva = int(input(f"Introduce el iva(4, 10 o 21)\n"))
        if (iva not in [4, 10, 21]):
            print("iva incorrect, se aplica el 21% por defecto\n")
            iva = 21
    except:
        print("iva incorrect, se aplica el 21% por defecto")
        iva = 21
    return valor * (1 + (iva/100))