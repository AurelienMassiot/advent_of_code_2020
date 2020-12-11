from main_day_11 import *


def test_is_occupied():
    # Given
    grid = [['#', '.'],
            ['#', '.']]

    # When Then
    assert is_occupied(grid, 0, 0)
    assert not is_occupied(grid, 0, 1)
    assert not is_occupied(grid, -1, -1)


def test_count_adjacent_occupied():
    # Given
    grid = [['#', '.'],
            ['#', '.']]

    # When Then
    assert count_adjacent_occupied(grid, 0, 0) == 1
    assert count_adjacent_occupied(grid, 1, 0) == 1
    assert count_adjacent_occupied(grid, 0, 1) == 2
    assert count_adjacent_occupied(grid, 1, 1) == 2


def test_count_ajacent_occupied_test_input():
    # Given
    grid = read_list_of_list('test_input.txt')
    grid = seat_all(grid)

    # When #Then
    assert count_adjacent_occupied(grid, 0, 0) == 2
    assert count_adjacent_occupied(grid, 1, 0) == 3
    assert count_adjacent_occupied(grid, 1, 1) == 6
    assert count_adjacent_occupied(grid, 0, 1) == 5
    assert count_adjacent_occupied(grid, 2, 2) == 6


def test_apply_one_unseat():
    # Given
    grid = read_list_of_list('test_input.txt')

    # When
    grid = seat_all(grid)
    grid = apply_unseat(grid, unseat_first_star(grid))
    grid = apply_seat(grid, seat_first_star(grid))

    # Then
    assert True


def test_play_first_star():
    # Given
    grid = read_list_of_list('test_input.txt')

    # When
    n_seats_occupied = play_first_star(grid)

    # Then
    assert n_seats_occupied == 37


def test_count_sight_occupied():
    # Given
    grid = [['#', '.'],
            ['#', '.']]

    # When Then
    assert count_sight_occupied(grid, 0, 1) == 2
    assert count_sight_occupied(grid, 1, 1) == 2

def test_second_star_case_1():
    # Given
    grid = read_list_of_list('test_input_2nd_star_1.txt')

    # When # Then
    assert count_sight_occupied(grid, 4, 3) == 8

def test_second_star_case_2():
    # Give2
    grid = read_list_of_list('test_input_2nd_star_2.txt')

    # When # Then
    assert count_sight_occupied(grid, 1, 1) == 0

def test_second_star_case_3():
    # Give2
    grid = read_list_of_list('test_input_2nd_star_3.txt')

    # When # Then
    assert count_sight_occupied(grid, 3, 3) == 0

def test_play_second_star():
    # Given
    grid = read_list_of_list('test_input.txt')

    # When
    n_seats_occupied = play_second_star(grid)

    # Then
    assert n_seats_occupied == 26