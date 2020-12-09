from main_day_9 import *

def test_is_valid_sum():
    # Given
    n_list_valid = [35, 20, 15, 25, 47, 40, 62, 55]
    n_list_invalid = [95, 102, 117, 150, 182, 127]
    preamble_number = 5

    # When # Then
    assert is_valid_sum(n_list_valid, 5, preamble_number)
    assert is_valid_sum(n_list_valid, 6, preamble_number)
    assert is_valid_sum(n_list_valid, 7, preamble_number)
    assert not is_valid_sum(n_list_invalid, 5, preamble_number)


def test_find_incorrect_number():
    # Given
    n_list = read_text_file_lines('test_input.txt')

    # When

    encryption_weakness = find_incorrect_number(n_list, 5)

    # Then
    assert encryption_weakness == 127


def test_find_encryption_weakness():
    # Given
    n_list = read_text_file_lines('test_input.txt')
    invalid_number = 127

    # When

    encryption_weakness = find_encryption_weakness(n_list, invalid_number)

    # Then
    assert encryption_weakness == 62
