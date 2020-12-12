from pprint import pprint

file_input = open("input.txt", "r")
txt = file_input.read().splitlines()

passports = []
cur_pass = set()

for line in txt:
    if line == '':
        passports.append(cur_pass)
        cur_pass = set()
        continue
    fields = line.split()
    for field in fields:
        key, val = field.split(':')
        cur_pass.add(key)

all_keys = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
])

cnt = 0
for passport in passports:
    diff = all_keys - passport
    if diff == set(['cid']) or len(diff) == 0:
        cnt += 1


print(cnt)
