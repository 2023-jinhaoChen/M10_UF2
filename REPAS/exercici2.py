valor = int(input("Introduce el valor(€)\n"))
iva = int(input("Introduce el porcentaje de IVA 4, 10 o 21(%)\n"))
valor_final = valor * (1 + (iva/100))
print(f"{valor}€ aplicando {iva}% de IVA es {valor_final}€")
