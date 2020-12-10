file_input = open("input.txt", "r")
txt = file_input.read().splitlines()

# tup def (low bound, high bound, letter, password)


def check_password(t: tuple):
    p = t[3]
    low_pos = t[0] - 1
    high_pos = t[1] - 1
    ltr = t[2]
    if (p[low_pos] == ltr and p[high_pos] == ltr):
        return False
    if (p[low_pos] == ltr or p[high_pos] == ltr):
        return True
    return False


cnt = 0

for line in txt:
    split_ln = line.split()
    low, high = split_ln[0].split('-')
    letter = split_ln[1].strip(':')
    password = split_ln[2]
    t = (int(low), int(high), letter, password)
    if check_password(t):
        cnt += 1

print(cnt)
