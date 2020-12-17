import os
from collections import defaultdict
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()
num_list = list(map(lambda x: int(x), txt))

num_list.append(0)

num_list.sort()
num_list.reverse()
max_num = max(num_list)
# num_set = set(num_list)

count_map = defaultdict(lambda: 0)  # adapter -> num of combinations
count_map[max_num] = 1

for num in num_list:
    if num in count_map.keys():
        continue
    for interval in (1, 2, 3):
        check_num = num + interval
        if check_num in count_map.keys():
            count_map[num] += count_map[check_num]

print(count_map)
