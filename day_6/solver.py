import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()

total = 0
row = set()

for i in range(len(txt)):
    line = txt[i]
    for ltr in line:
        row.add(ltr)
    if not line or i == len(txt) - 1:
        total += len(row)
        row = set()

print(total)