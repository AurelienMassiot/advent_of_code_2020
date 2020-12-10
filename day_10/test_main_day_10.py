from main_day_10 import *


def test_first_star_test_input():
    # Given
    n_list = read_text_file_lines('test_input.txt')

    # When
    n_list.append(0)
    n_list.append(max(n_list) + 3)
    n_list.sort()
    jolts_differences = substract_previous(n_list)
    counts = Counter(jolts_differences)

    # Then
    assert counts[1] == 7
    assert counts[3] == 5


def test_first_star_test_input_2():
    # Given
    n_list = read_text_file_lines('test_input_2.txt')

    # When
    n_list.append(0)
    n_list.append(max(n_list) + 3)
    n_list.sort()
    jolts_differences = substract_previous(n_list)
    counts = Counter(jolts_differences)

    # Then
    assert counts[1] == 22
    assert counts[3] == 10


def test_find_combinations():
    # Given
    n_list = [0, 1, 4, 5, 6, 9]

    # When
    n_combinations = compute_combinations(n_list, 0)

    # Then
    assert n_combinations == 2

def test_second_star_test_input():
    # Given
    n_list = read_text_file_lines('test_input.txt')

    # When
    n_list.append(0)
    n_list.append(max(n_list) + 3)
    n_list.sort()
    n_combinations = compute_combinations(n_list, 0)

    # Then
    assert n_combinations == 8

def test_second_star_test_input_2():
    # Given
    n_list = read_text_file_lines('test_input_2.txt')

    # When
    n_list.append(0)
    n_list.append(max(n_list) + 3)
    n_list.sort()
    n_combinations = compute_combinations(n_list, 0)

    # Then
    assert n_combinations == 19208
