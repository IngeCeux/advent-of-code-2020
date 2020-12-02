import re

input_file = open("input/day2.txt")
lines = str(input_file.read())
lines = lines.split('\n')


def isValidPart1(line):
    lower_bound = int(re.findall(r"(.*)-.*", line)[0])
    upper_bound = int(re.findall(r".*-(.*) .:.*", line)[0])
    character = re.findall(r".* (.):.*", line)[0]
    password = re.findall(r".*: (.*)", line)[0]

    if lower_bound <= password.count(character) <= upper_bound:
        return True
    else:
        return False


def isValidPart2(line):
    index1 = int(re.findall(r"(.*)-.*", line)[0]) - 1
    index2 = int(re.findall(r".*-(.*) .:.*", line)[0]) - 1
    character = re.findall(r".* (.):.*", line)[0]
    password = re.findall(r".*: (.*)", line)[0]

    # 'is not' is an exclusive or --> one or the other, not both
    if (password[index1] == character) is not (password[index2] == character):
        return True
    else:
        return False


count = 0

for line in lines:
    if isValidPart1(line):
        count += 1

print(count)

count = 0

for line in lines:
    if isValidPart2(line):
        count += 1

print(count)
