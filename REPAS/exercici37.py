def amb_iva(ftotal, iva = 21):
    return (ftotal * (1 + (iva/100)))

ftotal = float(input('Introdueix el preu de tot el carrito: '))

print(amb_iva(ftotal))


