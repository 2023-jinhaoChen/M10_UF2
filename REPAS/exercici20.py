diccionari = {}
nom = ""
while (True):
    nom = input("Introduce un nombre o salir para terminar el programa ")
    if nom == "salir":
        break
    if nom in diccionari.keys():
        print("ya existe este nombre")
        continue
    edad = input("Introduce la edad ")
    diccionari.update({nom:edad})
print(diccionari)
