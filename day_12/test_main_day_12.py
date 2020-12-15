from main_day_12 import *


def test_parse_instruction():
    # Given
    instruction = 'R90'

    # When Then
    assert parse_instruction(instruction) == ('R', 90)


def test_manhattan_distance_from_start_pos():
    # Given
    current_pos = (17, -8)

    # When Then
    assert manhattan_distance_from_start_pos(current_pos) == 25


def test_get_new_direction():
    # Given When Then
    assert get_new_direction('E', 1, 90) == 'S'
    assert get_new_direction('E', -1, 90) == 'N'


def test_rotate_waypoint():
    # Given When Then
    assert rotate_waypoint((10, 4), 'R', 90) == (4, -10)


def test_count_clockwise_quarter_turns():
    # Given When Then
    assert count_clockwise_quarter_turns('R', 90) == 1
    assert count_clockwise_quarter_turns('L', 90) == 3


def test_move_first_star():
    # Given When Then
    assert move_first_star((0, 0), 'E', ('F', 10)) == ((10, 0), 'E')
    assert move_first_star((17, 3), 'E', ('R', 90)) == ((17, 3), 'S')


def test_move_second_star():
    # Given When Then
    assert move_second_star((0, 0), (10, 1), ('S', 2)) == ((0, 0), (10, -1))


def test_navigate_first_star():
    # Given
    instructions = read_text_file_lines('test_input.txt')
    instructions = [parse_instruction(i) for i in instructions]

    # When
    final_pos = navigate_first_star(instructions)

    # Then
    assert final_pos == (17, -8)
    assert manhattan_distance_from_start_pos(final_pos) == 25


def test_navigate_second_star():
    # Given
    instructions = read_text_file_lines('test_input.txt')
    instructions = [parse_instruction(i) for i in instructions]

    # When
    final_pos = navigate_second_star(instructions)

    # Then
    assert final_pos == (214, -72)
    assert manhattan_distance_from_start_pos(final_pos) == 286


8
