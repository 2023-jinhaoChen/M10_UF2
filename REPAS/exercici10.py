import random
found = False
guesses = 0
number = random.randint(1,100)
while (not found):
    guess = int(input("Introduce un número entre 1 y 100\n"))
    guesses += 1
    if (guess == number):
        found = True
        print(f"Has endivinado el número, número es {number}, numero de intentos: {guesses}")
    elif (guess < number):
        print("El número es más grande que el número introducido")
    else:
        print("El número es más pequeño que el número introducido")