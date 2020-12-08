input_file = open("input/day8.txt")
lines = str(input_file.read())
lines = lines.split('\n')

accumulator = 0
visited_indexes = []
instructions = []


def parse_value(value_string):
    value_string.replace('+', '')
    return int(value_string)


for line in lines:
    command = line.split(' ')[0]
    value = parse_value(line.split(' ')[1])
    instructions.append((command, value))


def execute_instructions(adapted_instructions):
    visited_indexes = []
    accumulator = 0
    index = 0
    while index < len(adapted_instructions):
        command = adapted_instructions[index][0]
        value = adapted_instructions[index][1]
        if command == 'acc':
            accumulator += value
            index += 1
        elif command == 'jmp':
            index += value
        elif command == 'nop':
            index += 1

        if index in visited_indexes:
            return None

        visited_indexes.append(index)

    return accumulator


for i in range(len(instructions)):
    adapted_instructions = instructions.copy()
    if adapted_instructions[i][0] == 'jmp':
        adapted_instructions[i] = ('nop', adapted_instructions[i][1])
    elif adapted_instructions[i][0] == 'nop':
        adapted_instructions[i] = ('jmp', adapted_instructions[i][1])
    result = execute_instructions(adapted_instructions)
    if result != None:
        print(result)
        break
