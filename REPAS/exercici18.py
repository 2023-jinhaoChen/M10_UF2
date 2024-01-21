text = input("Introduce 2 parablas\n")
text_without_repeats= ""
for char in text:
    if char is " ":
        continue
    if char not in text_without_repeats:
        text_without_repeats += char
text_without_repeats = tuple(text_without_repeats)
for char in text_without_repeats:
    print(f"{char} ha salido {text.count(char)} veces")