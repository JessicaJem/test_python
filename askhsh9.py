import string
import math

with open("two_cities_ascii.txt", "r") as f:
    text = f.read()
    print(text)
    words = text.split()
    print(words)
    table = str.maketrans("", "", string.punctuation)
    stripped_list = [w.translate(table) for w in words]
    print(stripped_list)

with open('two_cities_ascii.txt', 'r') as f:
    file_contents = f.read()

stripped_list = [ord(char) for char in file_contents]
print(stripped_list)
count = 0
lista1 = [0 for i in range(13)]
for i in range(len(stripped_list)):
    if stripped_list[i] % 2 == 1:
        if 97 <= stripped_list[i] <= 121:
            lista1[(stripped_list[i] - 97) // 2] += 1
            count += 1
        elif stripped_list[i] % 2 == 0:
            print(stripped_list[i])
            del stripped_list[i]
print(lista1)
k = 0
for i in range(97, 122, 2):
    print(chr(i), ":", math.ceil(lista1[k] / count * 100) * "*")
    k += 1
