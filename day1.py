input_file = open("input/day1.txt")
lines = str(input_file.read())
lines = lines.split('\n')

numbers=[]

for line in lines:
    numbers.append(int(line))

numbers.sort()

toRemove = []
for number in numbers:
    if (number + numbers[0]) > 2020:
        toRemove.append(number)

for number in toRemove:
    numbers.remove(number)


def part1():
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (numbers[i] + numbers[j]) == 2020:
                print(numbers[i]*numbers[j])
                return

def part2():
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k]) > 2020:
                    break
                elif (numbers[i] + numbers[j] + numbers[k]) == 2020:
                    print(numbers[i]*numbers[j]*numbers[k])
                    return

part1()
part2()