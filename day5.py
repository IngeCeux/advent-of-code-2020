import math

input_file = open("input/day5.txt")
lines = str(input_file.read())
lines = lines.split('\n')


def first_half(rows):
    upper = math.floor(rows[1] - (rows[1]-rows[0])/2)
    return (rows[0], upper)


def last_half(rows):
    lower = math.ceil(rows[0] + (rows[1]-rows[0])/2)
    return (lower, rows[1])


def getSeat(line):
    rows = (0, 127)
    for i in range(6):
        if line[i] == 'F':
            rows = first_half(rows)
        else:
            rows = last_half(rows)

    if line[6] == 'F':
        row = rows[0]
    else:
        row = rows[1]

    columns = (0, 7)
    for i in range(7, 9):
        if line[i] == 'L':
            columns = first_half(columns)
        else:
            columns = last_half(columns)

    if line[9] == 'L':
        column = columns[0]
    else:
        column = columns[1]

    return (row, column)


def get_id(seat):
    return seat[0] * 8 + seat[1]


seat_ids = []

for line in lines:
    seat = getSeat(line)
    seat_id = get_id(seat)
    seat_ids.append(seat_id)

print('max: ', max(seat_ids))

seats = []

missing = []
missing_ids = []

for line in lines:
    seat = getSeat(line)
    seats.append(seat)

for i in range(128):
    for j in range(8):
        if (i, j) not in seats:
            missing.append((i, j))
            missing_ids.append(get_id((i, j)))

for i in range(len(missing_ids)):

    if missing_ids[i]-1 not in missing_ids and missing_ids[i]+1 not in missing_ids:
        print(missing_ids[i])
