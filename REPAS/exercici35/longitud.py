def parse_frase(frase=str):
    paraules = frase.split()
    len_dict = {}
    for paraula in paraules:
        len_dict[paraula] = len(paraula)
    return len_dict