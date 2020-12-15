from main_day_13 import *


def test_first_star():
    # Given
    first_departure, buses_with_offsets = parse_lines(read_input('test_input.txt'))

    # When # Then
    assert first_bus(first_departure, buses_with_offsets) == 295

def test_second_star_test_input():
    # Given
    first_departure, buses_with_offsets = parse_lines(read_input('test_input.txt'))

    # When # Then
    assert timestamp_sync(buses_with_offsets) == 1068781

def test_second_star_test_input_1():
    # Given
    first_departure, buses_with_offsets = parse_lines(read_input('test_input_second_star_1.txt'))

    # When # Then
    assert timestamp_sync(buses_with_offsets) == 3417

def test_second_star_test_input_2():
    # Given
    first_departure, buses_with_offsets = parse_lines(read_input('test_input_second_star_2.txt'))

    # When # Then
    assert timestamp_sync(buses_with_offsets) == 754018


def test_second_star_test_input_3():
    # Given
    first_departure, buses_with_offsets = parse_lines(read_input('test_input_second_star_3.txt'))

    # When # Then
    assert timestamp_sync(buses_with_offsets) == 779210

