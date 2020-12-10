from treelib import Node, Tree

input_file = open("input/day10.txt")
lines = str(input_file.read())
lines = lines.split('\n')

numbers = [0]

for line in lines:
    numbers.append(int(line))

numbers.sort()
numbers.append(numbers[-1]+3)

ones = 0
twos = 0
threes = 0

for i in range(1, len(numbers)):
    if numbers[i] - numbers[i-1] == 1:
        ones += 1
    elif numbers[i] - numbers[i-1] == 2:
        twos += 1
    elif numbers[i] - numbers[i-1] == 3:
        threes += 1

# print(ones * threes)

# PART 2

differences = []

for i in range(1, len(numbers)):
    differences.append(numbers[i] - numbers[i-1])

print(differences)

sequences = []

start = 0

for i in range(len(differences)):
    if differences[i] == 1:
        continue
    else:
        if len(differences[start:i]) > 0:
            sequences.append(differences[start:i])
        while differences[i] != 1:
            if i+1 < len(differences):
                i += 1
            else:
                break
        start = i
print(sequences)

result = 1

for sequence in sequences:
    if len(sequence) == 2:
        result *= 2
    elif len(sequence) == 3:
        result *= 4
    elif len(sequence) == 4:
        result *= 7

print(result)

# def get_children(index):
#     children = []
#     for i in range(4):
#         if index+i < len(numbers) and 0 < numbers[index+i]-numbers[index] <= 3:
#             children.append(numbers[index+i])
#     return children


# families = {}

# for i in range(len(numbers)):
#     children = get_children(i)
#     if len(children) > 1:
#         families[numbers[i]] = children


# def has_parent_in_families(index):
#     number = list(families)[index]
#     keys = list(families)[:index]
#     would_be_parents = [number-3, number-2, number-1]
#     for parent in would_be_parents:
#         if parent in keys:
#             return True
#     return False


# counting_family = False
# family_count = 0
# counts = []

# for i in range(len(families)):
#     key = list(families)[i]
#     if has_parent_in_families(i):
#         family_count += len(families.get(key)) - 1
#         counting_family = True
#     else:
#         if counting_family:
#             counts.append(family_count)
#             counting_family = False
#         family_count = len(families.get(key))


# print(counts)
