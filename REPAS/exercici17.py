text = input("Introduce una frase\n")
output_text= ""
for char in text:
    if char == " ":
        continue
    if char not in output_text:
        output_text += char
print(tuple(output_text))