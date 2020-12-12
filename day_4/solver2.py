import re

file_input = open("input.txt", "r")
txt = file_input.read().splitlines()

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


def validate_keys_present(p: dict):
    diff = all_keys - set(p.keys())
    if diff == set(['cid']) or len(diff) == 0:
        return True
    return False


def validate_byr(byr: str):
    try:
        byr = int(byr)
    except:
        return False
    return 1920 <= byr <= 2002


def validate_iyr(iyr: str):
    try:
        iyr = int(iyr)
    except:
        return False
    return 2010 <= iyr <= 2020


def validate_eyr(eyr: str):
    try:
        eyr = int(eyr)
    except:
        return False
    return 2020 <= eyr <= 2030


def validate_hgt(hgt: str):
    try:
        unit = hgt[-2:]
        num = int(hgt[:-2])
    except Exception as e:
        return False
    if unit.lower() not in {'cm', 'in'}:
        return False
    if unit.lower() == 'cm':
        return 150 <= num <= 193
    return 59 <= num <= 76


def validate_hcl(hcl: str):
    regex = '^#[0-9a-f]{6}$'
    return re.match(regex, hcl)


def validate_ecl(ecl: str):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def validate_pid(pid:str):
    regex = '^[0-9]{9}$'
    return re.match(regex, pid)


def validate_keys(p: dict):
    if not validate_byr(p.get('byr')):
        return False
    if not validate_iyr(p.get('iyr')):
        return False
    if not validate_eyr(p.get('eyr')):
        return False
    if not validate_hgt(p.get('hgt')):
        return False
    if not validate_hcl(p.get('hcl')):
        return False
    if not validate_ecl(p.get('ecl')):
        return False
    if not validate_pid(p.get('pid')):
        return False
    return True


def validate_passport(p: dict):
    if not validate_keys_present(p):
        return False
    return validate_keys(p)


passports = []
cur_pass = dict()

cnt = 0

for line in txt:
    if line == '':
        if validate_passport(cur_pass):
            cnt += 1
        cur_pass = dict()
        continue
    fields = line.split()
    for field in fields:
        key, val = field.split(':')
        cur_pass[key] = val

print(cnt)
