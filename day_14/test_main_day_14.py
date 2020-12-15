from main_day_14 import *


def test_apply_binary_mask_str_to_binary_number_str():
    # Given When Then
    assert apply_binary_mask_str_to_binary_number_str(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 73
    assert apply_binary_mask_str_to_binary_number_str(101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 101
    assert apply_binary_mask_str_to_binary_number_str(0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 64


def test_memory_sum_1():
    # Given
    program = read_text_file_lines('test_input.txt')

    # When Then
    assert memory_sum_1(program) == 165


def test_memory_sum_2():
    # Given
    program = read_text_file_lines('test_input_2.txt')

    # When Then
    assert memory_sum_2(program) == 208
