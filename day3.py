input_file = open("input/day3.txt")
lines = str(input_file.read())
lines = lines.split('\n')

x_pos = 0

trees = 0

for line in lines:
    if x_pos >= len(line):
        x_pos = x_pos - len(line)
    if line[x_pos] == '#':
        trees += 1
    x_pos += 3

print(trees)


def part2(right, down):
    x_pos = 0
    trees = 0
    for i in range(0, len(lines), down):
        if x_pos >= len(lines[i]):
            x_pos = x_pos - len(lines[i])
        if lines[i][x_pos] == '#':
            trees += 1
        x_pos += right
    return trees


result = part2(1, 1) * part2(3, 1) * part2(5, 1) * part2(7, 1) * part2(1, 2)

print(result)
