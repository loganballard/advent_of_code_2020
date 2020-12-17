import os
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()
num_list = list(map(lambda x: int(x), txt))

num_list.sort()

prev_val = 0
count_1 = 0
count_3 = 1


for num in num_list:
    diff = num - prev_val
    if diff == 1:
        count_1 += 1
    elif diff == 3:
        count_3 += 1
    prev_val = num

print(count_1, count_3)

print("answer: ", count_1*count_3)
