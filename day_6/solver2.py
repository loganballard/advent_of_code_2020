import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()

total = 0
row = []
person = set()

for i in range(len(txt)):
    line = txt[i]
    if line:
        for ltr in line:
            person.add(ltr)
        row.append(person)
        person = set()
    if not line or i == len(txt) - 1:
        intersection = set(row[0])
        for p in row[1:]:
            intersection = intersection & p
        total += len(intersection)
        row = []

print(total)