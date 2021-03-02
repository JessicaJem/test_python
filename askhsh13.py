import string

with open("two_cities_ascii.txt", "r") as f:
    text = f.read()
    print(text)
    words = text.split()
    print(words)
    table = str.maketrans("", "", string.punctuation)
    stripped_list = [w.translate(table) for w in words]
    print(stripped_list)

pos1 = 0
pos2 = 0
while pos1 < len(stripped_list):
    if pos2 == len(stripped_list):
        pos1 += 1
        pos2 = 0
    elif pos1 == pos2:
        pos2 += 1
        if pos2 >= len(stripped_list):
            pos1 += 1
            pos2 = 0
    if pos1 < len(stripped_list) and pos2 < len(stripped_list):
        if len(stripped_list[pos1]) + len(stripped_list[pos2]) == 20:
            print(stripped_list[pos1] + stripped_list[pos2])
            del stripped_list[pos1]
            del stripped_list[pos2]
    pos2 += 1
