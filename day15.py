input_file = open("input/day15.txt")
line = str(input_file.read())
numbers = line.split(',')

numbers = [int(i) for i in numbers]

# spoken = []


# def consider_last_spoken():
#     last_spoken = spoken[-1]
#     # print(last_spoken)
#     to_speak = 0
#     if spoken.count(last_spoken) >= 2:
#         for i in reversed(range(len(spoken)-1)):
#             if spoken[i] == last_spoken:
#                 # print('found', i)
#                 to_speak = len(spoken)-1 - i
#                 break
#     spoken.append(to_speak)
#     return to_speak


# for number in numbers:
#     spoken.append(number)

# end = 2020

# for i in range(len(numbers), end):
#     last = consider_last_spoken()
#     if i == end:
#         print('turn ', i+1, ':', last)


# Part 2

spoken = {}
last_spoken = 0
turn = 1


def consider_last_spoken2(last_spoken, turn):
    to_speak = 0
    if len(spoken.get(last_spoken)) > 1:
        last_index = spoken.get(last_spoken)[-2]
        # print('found', last_spoken, "at", last_index)
        to_speak = spoken.get(last_spoken)[-1] - last_index
    if to_speak not in spoken.keys():
        spoken[to_speak] = [turn]
    else:
        spoken.get(to_speak).append(turn)
    return to_speak


for number in numbers:
    spoken[number] = [turn]
    last_spoken = number
    # print('turn ', turn, ':', last_spoken)
    turn += 1

end = 30000000

for i in range(turn, end+1):
    last_spoken = consider_last_spoken2(last_spoken, turn)
    # print(spoken)
    # print('turn ', turn, 'speaks:', last_spoken)

    if turn == end:
        print('turn ', turn, 'speaks:', last_spoken)
        break
    turn += 1
