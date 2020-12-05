import re

input_file = open("input/day4.txt")
lines = str(input_file.read())
passports = lines.split('\n\n')

required = [
    'byr:(19[2-8][0-9]|199[0-9]|200[0-2])',
    'iyr:(201[0-9]|2020)',
    'eyr:(202[0-9]|2030)',
    'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',
    'hcl:#[0-9a-f]{6}',
    'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
    'pid:[0-9]{9}']


def is_valid(passport):
    for field in required:
        pattern = re.compile(field)
        if re.search(pattern, passport) is None:
            return False
    print(passport, '\n')
    return True


count = 0

for passport in passports:
    if is_valid(passport):
        count += 1

print(count)
