file_input = open("input.txt", "r")
txt = file_input.read().splitlines()
num_arr = []

for n in txt:
    num_arr.append(int(n))

num_arr.sort()
num_rev_arr = num_arr.copy()
num_set = set(num_arr)

done = False

for i in range(len(num_arr)):
    number = num_arr[i]
    for big_num in num_arr[i:]:
        total = number + big_num
        if total > 2020:
            break
        target = 2020 - total
        if target in num_set and (target != number and target != big_num):
            print("nailed it")
            print(f"num_1: {number}")
            print(f"num_2: {big_num}")
            print(f"num_3: {target}")
            print(f"total: {number * big_num * target}")
            done = True
            break
    if done:
        break


