file_input = open("input.txt", "r")
txt = file_input.read().splitlines()

def is_even(n):
    return n % 2 == 0

def get_half(st, lo, hi):
    for ltr in st:
        range_nums = hi - lo
        half = range_nums // 2
        if is_even(range_nums):
            half -= 1
        if ltr == 'F' or ltr == 'L':
            hi = lo + half
        else:
            lo = lo + half + 1
    if lo != hi:
        exit("uh oh")
    return lo


def get_seat_id(row, col):
    return (row * 8) + col

cur_highest = 0
for st in txt:
    row = get_half(st[0:7], 0, 127) # rows
    col = get_half(st[7:], 0, 7) # seats
    seat_id = get_seat_id(row, col)
    if seat_id > cur_highest:
        cur_highest = seat_id

print(cur_highest)
