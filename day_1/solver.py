file_input = open("input.txt", "r")
txt = file_input.read().splitlines()
num_arr = []

for n in txt:
    num_arr.append(int(n))

num_arr.sort()

i = 0
j = len(num_arr) - 1

while i < j:
    num_lo = num_arr[i]
    num_hi = num_arr[j]
    if num_lo + num_hi == 2020:
        print("nailed it")
        print(num_lo, num_hi, (num_lo * num_hi))
        break
    if num_lo + num_hi > 2020:
        j -= 1
        i = 0
        continue
    i += 1


