input_file = open("input/day6.txt")
lines = str(input_file.read())
groups = lines.split('\n\n')


def count_yes(group):
    yes = ''
    group = group.replace('\n', '')
    for char in group:
        if char not in yes:
            yes += char
    if len(group) < 10:
        print(group)
        print('yes', yes)
    return len(yes)


# count = 0

# for group in groups:
#     count += count_yes(group)

# print(count)


def count_yes_2(group):
    people = group.split('\n')
    result = set(people[0])
    if len(people) > 1:
        for i in range(1, len(people)):
            result = set(result).intersection(people[i])
    if len(group) < 10:
        print(group)
        print('overlap', result, len(result))
    return len(result)


count = 0

for group in groups:
    count += count_yes_2(group)

print(count)
