words = input("introduce 2 parablas\n").split()
first_word = words[0]
second_word = words[1]
new_first_word = second_word[0:2] + first_word[2:]
new_second_word = first_word[0:2] + second_word[2:]
print(new_first_word, new_second_word)