input_file = open("input/day11.txt")
lines = str(input_file.read())
rows = lines.split('\n')

new_rows = []

row_length = len(rows[0])


def direction_occupied(i, j, ver, hor):
    y = i + ver
    x = j + hor
    while 0 <= y < len(rows) and 0 <= x < row_length:
        if rows[y][x] == '#':
            return True
        elif rows[y][x] == 'L':
            return False
        y += ver
        x += hor
    return False


# def count_adjacent(i, j):
#     lower_i = i-1 if i > 0 else i
#     lower_j = j-1 if j > 0 else j
#     upper_i = i+1 if i < len(rows)-1 else i
#     upper_j = j+1 if j < row_length-1 else j

#     count = 0
#     for i2 in range(lower_i, upper_i+1):
#         for j2 in range(lower_j, upper_j+1):
#             if (i2, j2) != (i, j) and rows[i2][j2] == '#':
#                 count += 1
#     return count

def count_adjacent(i, j):
    count = 0
    for y in range(-1, +2):
        for x in range(-1, +2):
            if (x, y) != (0, 0):
                if direction_occupied(i, j, y, x):
                    count += 1
    return count


def arrays_equal(array1, array2):
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True


def print_rows(rows):
    for row in rows:
        print(row)
    print('\n')


while True:
    for i in range(len(rows)):
        row = ''
        adjacent_row = ''

        for j in range(row_length):
            adjecent = count_adjacent(i, j)
            if rows[i][j] == '.':
                adjacent_row += '.'
            else:
                adjacent_row += str(adjecent)

            if rows[i][j] == '.':
                row += '.'
            elif rows[i][j] == 'L':
                if adjecent == 0:
                    row += '#'
                else:
                    row += 'L'
            else:
                if adjecent >= 5:
                    row += 'L'
                else:
                    row += '#'
        new_rows.append(row)

    if arrays_equal(rows, new_rows):
        break
    else:
        rows = new_rows
        new_rows = []


result = 0
for i in range(len(rows)):
    for j in range(row_length):
        if rows[i][j] == '#':
            result += 1

print(result)
