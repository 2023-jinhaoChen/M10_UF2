areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(f"el segon element: {areas_pis[1]}")
print(f"el últim element: {areas_pis[-1]}")
print(f"l'àrea de la terrassa: {areas_pis[7]}")
print(f"primer al tercer element: ", end="")
for i in areas_pis[0:3]:
    print(i, end=" ")
print()
print(f"tercer al tercer element: ", end="")
for i in areas_pis[3:]:
    print(i, end=" ")
print("")

print(f"total de l'àrea de les dues habitacions: {areas_pis[5]+areas_pis[-1]}")

areas_pis[9] = 4.55
print("despues de modificar area de lavabo: ", end=" ") 
print(areas_pis)

areas_pis.append("pati interior")
areas_pis.append("2.78")
print("despues de añadir pati inteiror: ", end=" ") 
print(areas_pis)

total_areas = 0
for area in areas_pis[1::2]:
    total_areas+=float(area)
print(f"total de l'àrea del pis: {total_areas}")

# Modificar l’àrea del lavabo i imprimir la nova list area
# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
# Imprimir el total de l’àrea del pis.

