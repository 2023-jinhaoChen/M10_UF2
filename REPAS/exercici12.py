months = ("enero", "febrero", "marzo", "abril", "mayo", "junio" \
          ,  "julio", "agosto", "septiembre", "octubre", \
            "noviembre", "diciembre")
exit = False
while (not exit):
    number = int(input("Introduce el número entre 1-12 o 0 para salir\n"))
    if (number is not 0):
        print(months[number-1])
    else:
        exit = True
