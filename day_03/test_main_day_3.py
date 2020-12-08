from main_day_3 import read_array, move, traverse_map


def test_normal_move():
    # Given
    x, y = 0, 0
    move_down, move_right = 1, 3
    expected_x_y = 1, 3
    wide = 10

    # When
    end_pos = move(wide, x, y, move_down, move_right)

    # Then
    assert end_pos == expected_x_y


def test_move_too_much_right():
    # Given
    x, y = 0, 9
    move_down, move_right = 1, 3
    expected_x_y = 1, 2
    wide = 10

    # When
    end_pos = move(wide, x, y, move_down, move_right)

    # Then
    assert end_pos == expected_x_y


def test_traverse_map_first_line():
    # Given
    map = [['..##'],
           ['#...']]
    move_down, move_right = 1, 3
    expected_n_trees = 0

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_second_line():
    # Given
    map = [['.#..'],
           ['...#']]
    move_down, move_right = 1, 3
    expected_n_trees = 1

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_two_first_lines():
    # Given
    map = [['..##...'],
           ['#...#..'],
           ['.#....#']]
    move_down, move_right = 1, 3
    expected_n_trees = 1

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_full_puzzle_right_3_down_1():
    # Given
    map = read_array('test_input.txt')
    move_down, move_right = 1, 3
    expected_n_trees = 7

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_full_puzzle_right_1_down_1():
    # Given
    map = read_array('test_input.txt')
    move_down, move_right = 1, 1
    expected_n_trees = 2

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_full_puzzle_right_5_down_1():
    # Given
    map = read_array('test_input.txt')
    move_down, move_right = 1, 5
    expected_n_trees = 3

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_full_puzzle_right_7_down_1():
    # Given
    map = read_array('test_input.txt')
    move_down, move_right = 1, 7
    expected_n_trees = 4

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees


def test_traverse_map_full_puzzle_right_1_down_2():
    # Given
    map = read_array('test_input.txt')
    move_down, move_right = 2, 1
    expected_n_trees = 2

    # When
    n_trees = traverse_map(map, move_down, move_right)

    # Then
    assert n_trees == expected_n_trees
