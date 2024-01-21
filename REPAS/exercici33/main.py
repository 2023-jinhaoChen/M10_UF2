from iva import calcular_iva


def aplicar_descuento(valor, descuento):
    return (valor * (1 - (descuento/100)))

lista_de_compra = {100:10,
                   250:5,
                   1500:30}

for count, compra in enumerate(lista_de_compra):
    valor_list = []
    descuento_list = []
    for valor in lista_de_compra:
        valor_list.append(valor)
        descuento_list.append(lista_de_compra.get(valor))
    print(f"Producte {count + 1}: preu inicial: {valor_list[count]}, descuento: {descuento_list[count]}")
    print(f"preu final: {calcular_iva(aplicar_descuento(valor_list[count], descuento_list[count]))}")