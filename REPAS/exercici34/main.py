from functions import quadrat
from functions import my_map

list = list(range(10))

list_quadrat = my_map(quadrat, list)
print(list_quadrat)