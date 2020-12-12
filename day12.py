input_file = open("input/day12.txt")
lines = str(input_file.read())
lines = lines.split('\n')

directions = ['N', 'E', 'S', 'W']

x = 0
y = 0

facing = 1


def turn(direction, degrees):
    global facing
    index_mod = int(degrees / 90)
    if direction == 'L':
        index_mod = -index_mod
    facing += index_mod
    while facing >= len(directions):
        facing -= 4
    while 0 > facing:
        facing += 4
    print(facing)


def move(direction, value):
    global x, y
    if direction == 'F':
        direction = directions[facing]
    elif direction in ['L', 'R']:
        turn(direction, value)
        return

    if direction == 'N':
        y += value
    elif direction == 'S':
        y -= value
    elif direction == 'E':
        x += value
    elif direction == 'W':
        x -= value


# for line in lines:
#     move(line[0], int(line[1:]))

# print('result:', abs(x)+abs(y))

# PART 2

x = 0
y = 0

waypoint_x = 10
waypoint_y = 1


def turn_waypoint(direction, degrees):
    global waypoint_x, waypoint_y
    turns = int(degrees / 90)
    if direction == 'R':
        for i in range(turns):
            temp_x = waypoint_x
            waypoint_x = waypoint_y
            waypoint_y = -temp_x
    else:
        for i in range(turns):
            temp_y = waypoint_y
            waypoint_y = waypoint_x
            waypoint_x = -temp_y


def move2(direction, value):
    global waypoint_x, waypoint_y, x, y

    if direction == 'F':
        x += value * waypoint_x
        y += value * waypoint_y
    elif direction in ['L', 'R']:
        turn_waypoint(direction, value)
    elif direction == 'N':
        waypoint_y += value
    elif direction == 'S':
        waypoint_y -= value
    elif direction == 'E':
        waypoint_x += value
    elif direction == 'W':
        waypoint_x -= value


for line in lines:
    move2(line[0], int(line[1:]))

print('result:', abs(x)+abs(y))
