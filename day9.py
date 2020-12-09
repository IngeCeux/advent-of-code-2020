input_file = open("input/day9.txt")
lines = str(input_file.read())
lines = lines.split('\n')

numbers = []
preamble_size = 25

for line in lines:
    numbers.append(int(line))


def get_invalid_number(number, preamble):
    for value1 in preamble:
        for value2 in preamble:
            if value1 != value2:
                if value1 + value2 == number:
                    return None
    return number


for i in range(preamble_size, len(numbers)):
    invalid = get_invalid_number(numbers[i], numbers[(i-preamble_size):i])
    if invalid is not None:
        print(invalid)
        break

for i in range(len(numbers)):
    weakness = []
    count = 0
    index = i
    while not count > invalid:
        if numbers[index] != invalid:
            count += numbers[index]
            weakness.append(numbers[index])
            if count == invalid:
                print(min(weakness) + max(weakness))
        index += 1
