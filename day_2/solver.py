file_input = open("input.txt", "r")
txt = file_input.read().splitlines()

# tup def (low bound, high bound, letter, password)


def check_password(t: tuple):
    cnt = 0
    for ltr in t[3]:
        if ltr == t[2]:
            cnt += 1
    if t[0] <= cnt <= t[1]:
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
