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
    return target


what_is_our_number = -1


for i in range(preamble_len, len(num_list)):
    prev_nums = num_list[i-preamble_len:i]
    num = num_list[i]
    target = is_valid_preamble(num, prev_nums)
    if target == True:
        continue
    what_is_our_number = target
    break

## Warning, brute force ahead:

for i in range(len(num_list)):
    total = num_list[i]
    for j in range(i+1, len(num_list)):
        total += num_list[j]
        if total == what_is_our_number:
            list_slice = num_list[i:j+1]
            lo, hi = min(list_slice), max(list_slice)
            print(f"low + high: {lo + hi}")
            break
        if total > what_is_our_number:
            break