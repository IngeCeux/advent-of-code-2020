import re
import itertools

input_file = open("input/day16.txt")
lines = str(input_file.read())
parts = lines.split('\n\n')

rule_lines = parts[0].split('\n')
your_ticket = parts[1].split('\n')[1]
your_ticket = [int(i) for i in your_ticket.split(',')]
print(your_ticket)
nearby_tickets = parts[2].split('\n')[1:]

rule_pattern = '(.*): (.*)-(.*) or (.*)-(.*)'

rules = {}

for rule in rule_lines:
    bounds = re.findall(rule_pattern, rule)[0]
    rules[bounds[0]] = [int(i) for i in bounds[1:]]
# print(rules)


def follows_rule(number, rule):
    result = False

    if (rule[0] <= number <= rule[1]) or (rule[2] <= number <= rule[3]):
        result = True
    else:
        result = False

    # print(rule[0], '<=', number, '<=', rule[1])
    # print(rule[2], '<=', number, '<=', rule[3])
    # print(result, '\n')
    return result


invalid_numbers = []


def check_ticket(ticket):
    ticket_numbers = ticket.split(',')
    ticket_numbers = [int(i) for i in ticket_numbers]
    ticket_valid = True
    for number in ticket_numbers:
        valid = False
        for rule in rules:
            if follows_rule(number, rules.get(rule)):
                valid = True
                break
        if not valid:
            invalid_numbers.append(number)
            ticket_valid = False
    return ticket_valid


to_remove = []

for ticket in nearby_tickets:
    if not check_ticket(ticket):
        to_remove.append(ticket)

for ticket in to_remove:
    nearby_tickets.remove(ticket)

print(sum(invalid_numbers))

# part 2

for i in range(len(nearby_tickets)):
    ticket = nearby_tickets[i]
    ticket = ticket.split(',')
    ticket = [int(i) for i in ticket]
    nearby_tickets[i] = ticket

possible_fields = []

ticket_length = len(nearby_tickets[0])

for i in range(ticket_length):
    possible_fields.append([rule for rule in rules.keys()])


def remove_field_from_all_except(field, index):
    for i in range(len(possible_fields)):
        if i != index and field in possible_fields[i]:
            possible_fields[i].remove(field)


for i in range(ticket_length):
    rule_found = False
    for ticket in nearby_tickets:
        for rule in possible_fields[i]:
            if not follows_rule(ticket[i], rules.get(rule)):
                possible_fields[i].remove(rule)
                if len(possible_fields[i]) == 1:
                    rule_found = True
                    remove_field_from_all_except(possible_fields[i][0], i)
                    break
        if rule_found:
            break

while max([len(i) for i in possible_fields]) != 1:
    for i in range(len(possible_fields)):
        other_lists = possible_fields[:i]
        other_lists.append(
            list(itertools.chain.from_iterable(possible_fields[i+1:])))
        other_lists = list(itertools.chain.from_iterable(other_lists))
        overlap = [x for x in possible_fields[i] if x in set(other_lists)]
        if len(possible_fields[i]) - len(overlap) == 1:
            possible_fields[i] = [
                i for i in possible_fields[i] if i not in overlap]

values = []

for i in range(len(possible_fields)):
    if 'departure' in possible_fields[i][0]:
        values.append(your_ticket[i])

result = 1

for value in values:
    result *= value

print(result)
