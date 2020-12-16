import os
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()
num_list = list(map(lambda x: int(x), txt))

preamble_len = 25

def is_valid_preamble(target, previous_numbers):
    prev_num_set = set(previous_numbers)
    first_num = prev_num_set.pop()
    while prev_num_set:
        other_num = target - first_num
        if other_num in prev_num_set:
            return True
        first_num = prev_num_set.pop()
    print(f"invalid: {target}")
    return False


for i in range(preamble_len, len(num_list)):
    prev_nums = num_list[i-preamble_len:i]
    num = num_list[i]
    if is_valid_preamble(num, prev_nums):
        continue
    break