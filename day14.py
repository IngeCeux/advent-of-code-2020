import re
import itertools

input_file = open("input/day14.txt")
lines = str(input_file.read())
lines = lines.split('\n')

index_pattern = 'mem.(.*). = .*'
value_pattern = 'mem.* = (.*)'
mask_pattern = 'mask = (.*)'

memory = {}


def apply_mask(value, mask):
    bit_string = "{0:b}".format(value)
    bit_string = list(bit_string.zfill(36))
    for i in range(len(mask)):
        if mask[i] != 'X':
            bit_string[i] = mask[i]
    return int(''.join(bit_string), 2)


def write_to_mem(index, value, mask):
    bit_string = "{0:b}".format(index)
    bit_string = list(bit_string.zfill(36))
    for i in range(len(mask)):
        if mask[i] == '1':
            bit_string[i] = mask[i]
    x_indexes = [i for i in range(len(mask)) if mask[i] == 'X']
    options = list(itertools.product(['1', '0'], repeat=len(x_indexes)))

    for i in range(len(options)):
        for j in range(len(options[i])):
            bit_string[x_indexes[j]] = options[i][j]
        memory[int(''.join(bit_string), 2)] = value


mask = ''

for line in lines:
    if 'mask' in line:
        mask = re.search(mask_pattern, line).group(1)
    else:
        index = int(re.search(index_pattern, line).group(1))
        value = int(re.search(value_pattern, line).group(1))
        # memory[index] = apply_mask(value, mask)
        write_to_mem(index, value, mask)


result = 0
for key, value in memory.items():
    if value != 0:
        result += value

print(result)
