import re

input_file = open("input/day7.txt")
lines = str(input_file.read())
lines = lines.split('\n')

# key can be in every value[]
rules = {}

container_pattern = '^(.*) bags contain'
content_pattern = '[0-9] ([a-z]* [a-z]*) bag'

for line in lines:
    container = re.search(container_pattern, line).group(1)
    values = re.findall(content_pattern, line)

    for color in values:
        if rules.get(color) != None:
            if container not in rules.get(color):
                rules[color].append(container)
        else:
            rules[color] = [container]

my_bag = 'shiny gold'

possible_containers = []


def find_containers(bag):
    if rules.get(bag):
        for color in rules[bag]:
            if color not in possible_containers:
                possible_containers.append(color)
                find_containers(color)


find_containers(my_bag)

print(len(possible_containers))

# ========= PART 2 =============

# key can be in every value[]
rules = {}

container_pattern = '^(.*) bags contain'
content_pattern = '([0-9] [a-z]* [a-z]*) bag'
amount_pattern = '([0-9])'
color_pattern = '([a-z].* [a-z].*)'

for line in lines:
    container = re.search(container_pattern, line).group(1)
    values = re.findall(content_pattern, line)

    colors = []

    for value in values:
        amount = int(re.search(amount_pattern, value).group(1))
        color = re.search(color_pattern, value).group(1)
        colors.append((color, amount))

        rules[container] = colors


def count_inner_bags(bag):
    count = 0
    if rules.get(bag):
        print(bag, '-->', rules.get(bag))
        for inner_bag in rules.get(bag):
            print(inner_bag)
            count += inner_bag[1] + inner_bag[1] * \
                count_inner_bags(inner_bag[0])
    else:
        count = 0
    print(bag, count, '\n')
    return count


print(count_inner_bags(my_bag))
print(rules[my_bag])
# print(rules)
