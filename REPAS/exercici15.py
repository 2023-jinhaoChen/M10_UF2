numbers = []
while (True):
    number = int(input("Introduce un número para añadir a la lista o 0 para salir\n"))
    if (number is 0):
        break
    else:
        numbers.append(number)
print(tuple(sorted(numbers)))

