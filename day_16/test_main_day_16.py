from main_day_16 import *


def test_parse_lines():
    # Given
    lines = read_text_file_lines('test_input.txt')

    # When
    rules, your_ticket, nearby_tickets = parse_lines(lines)

    # Then
    assert rules == [['class', range(1, 4), range(5, 8)],
                     ['row', range(6, 12), range(33, 45)],
                     ['seat', range(13, 41), range(45, 51)]]
    assert your_ticket == [7, 1, 14]
    assert nearby_tickets == [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]


def test_scanning_error_rate():
    # Given
    lines = read_text_file_lines('test_input.txt')
    rules, your_ticket, nearby_tickets = parse_lines(lines)

    # When
    error_rate, index_invalid_tickets = scanning_error_rate(rules, nearby_tickets)

    # Then
    assert error_rate == 71
    assert index_invalid_tickets == [1, 2, 3]


def test_discard_invalid_nearby_tickets():
    # Given
    nearby_tickets = [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]
    index_invalid_tickets = [1, 2, 3]

    # When
    clean_nearby_tickets = discard_invalid_nearby_tickets(nearby_tickets, index_invalid_tickets)

    #
    assert clean_nearby_tickets == [[7, 3, 47]]


def test_find_correct_rules_from_possible_rules():
    # Given
    possible_rules = {'class': [0, 1], 'row': [0], 'seat': [2]}

    # When
    order = find_correct_rules_from_possible_rules(possible_rules)

    # Then
    assert order == {'row': 0, 'seat': 2, 'class': 1}


def test_find_correct_rules():
    # Given
    rules, your_ticket, nearby_tickets = parse_lines(read_text_file_lines('test_input.txt'))
    _, index_invalid_tickets = scanning_error_rate(rules, nearby_tickets)
    clean_nearby_tickets = discard_invalid_nearby_tickets(nearby_tickets, index_invalid_tickets)

    # When
    order = find_correct_rules(rules, clean_nearby_tickets)

    # Then
    assert order == {'class': 1, 'row': 0, 'seat': 2}
