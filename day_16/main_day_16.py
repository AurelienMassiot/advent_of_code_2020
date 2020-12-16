from numpy import prod


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def parse_lines(lines):
    rules = []
    your_ticket = []
    nearby_tickets = []
    parsing_flag = 'rules'
    for line in lines:
        # print(line)
        if line == '':
            continue
        if line == 'your ticket:':
            parsing_flag = 'your_ticket'
            continue
        elif line == 'nearby tickets:':
            parsing_flag = 'nearby_tickets'
            continue
        if parsing_flag == 'rules':
            field = line.split(": ")[0]
            range1 = line.split(": ")[1].split(" or ")[0].split("-")
            range2 = line.split(": ")[1].split(" or ")[1].split("-")
            rules.append(
                [field, range(int(range1[0]), int(range1[1]) + 1), range(int(range2[0]), int(range2[1]) + 1)])
        elif parsing_flag == 'your_ticket':
            your_ticket = [int(x) for x in line.split(",")]
        elif parsing_flag == 'nearby_tickets':
            nearby_tickets.append([int(x) for x in line.split(",")])
    return rules, your_ticket, nearby_tickets


def scanning_error_rate(rules, nearby_tickets):
    invalid_tickets = []
    index_invalid_tickets = []
    # print('rules', rules)
    for i, ticket in enumerate(nearby_tickets):
        for value in ticket:
            # print('value', value)
            is_ticket_valid = False
            for rule in rules:
                if is_ticket_valid:
                    break
                for valid_range in rule[1:]:
                    # rint('valid_range', valid_range)
                    if value in valid_range:
                        is_ticket_valid = True
                        # print('valid')
                        break
            if not is_ticket_valid:
                invalid_tickets.append(value)
                index_invalid_tickets.append(i)
    # print('invalid tickets', invalid_tickets)
    return sum(invalid_tickets), index_invalid_tickets


def discard_invalid_nearby_tickets(nearby_tickets, index_invalid_tickets):
    return [i for j, i in enumerate(nearby_tickets) if j not in index_invalid_tickets]


def find_correct_rules_from_possible_rules(possible_rules):
    correct_rules = {}
    while len(possible_rules) > 0:
        new_correct_rules = {k: v[0] for k, v in possible_rules.items() if len(v) == 1}  # take obvious rules
        correct_rules.update(new_correct_rules)
        index_to_remove = [value for value in new_correct_rules.values()]
        yet_not_correct_rules = {k: v for k, v in possible_rules.items() if len(v) > 1}
        possible_rules = {}
        for key, possible_indices in yet_not_correct_rules.items():  # update possible rules without used indices
            possible_rules[key] = [indice for indice in possible_indices if indice not in index_to_remove]
    return correct_rules


def find_correct_rules(ranges, tickets):
    possible_rules = {r[0]: [] for r in ranges}
    n_tickets = len(tickets[0])
    for index in range(n_tickets):
        for r in ranges:
            if is_valid_index(index, r, tickets):
                field_name = r[0]
                possible_rules[field_name].append(index)
    correct_rules = find_correct_rules_from_possible_rules(possible_rules)
    return correct_rules


def is_valid_index(index, ranges, tickets):
    for ticket in tickets:
        if ticket[index] not in ranges[1] and ticket[index] not in ranges[2]:
            return False
    return True


def get_departure_indexes(order, rules):
    return [order[x] for x in [y[0] for y in rules] if 'departure' in x]


def get_product(rules, your_ticket, clean_nearby_tickets):
    order = find_correct_rules(rules, clean_nearby_tickets)
    departure_indexes = get_departure_indexes(order, rules)
    departure_numbers = [your_ticket[index] for index in departure_indexes]
    return prod(departure_numbers)


def first_star():
    rules, your_ticket, nearby_tickets = parse_lines(read_text_file_lines('input.txt'))
    error_rate, _ = scanning_error_rate(rules, nearby_tickets)
    return error_rate


def second_star():
    rules, your_ticket, nearby_tickets = parse_lines(read_text_file_lines('input.txt'))
    _, index_invalid_tickets = scanning_error_rate(rules, nearby_tickets)
    clean_nearby_tickets = discard_invalid_nearby_tickets(nearby_tickets, index_invalid_tickets)
    product = get_product(rules, your_ticket, clean_nearby_tickets)
    return product


if __name__ == "__main__":
    print(first_star())
    print(second_star())
