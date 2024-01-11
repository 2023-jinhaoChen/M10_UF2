numbers = input("Introduce 10 números separado por 1 espacio\n").split()
numbers = tuple(sorted(map(lambda x: int(x), numbers)))
print(numbers)
