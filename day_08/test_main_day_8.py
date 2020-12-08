from main_day_8 import *


def test_process_instruction():
    # Given
    instruction_1 = ('nop', +0)
    instruction_2 = ('acc', +3)
    instruction_3 = ('jmp', +3)
    instruction_4 = ('jmp', -1)

    # Given
    assert process_instruction(instruction_1, pos=0, acc=0, n_max_lines=10) == (1, 0)
    assert process_instruction(instruction_2, pos=0, acc=0, n_max_lines=10) == (1, 3)
    assert process_instruction(instruction_3, pos=0, acc=0, n_max_lines=10) == (3, 0)
    assert process_instruction(instruction_4, pos=1, acc=0, n_max_lines=10) == (0, 0)


def test_run_program():
    # Given
    lines = clean_lines(read_text_file_lines('test_input.txt'))

    # Given
    pos, acc = run_program(lines)

    # Then
    assert pos == 1
    assert acc == 5


def test_run_program_n_times_first_star():
    # Given
    lines = clean_lines(read_text_file_lines('test_input.txt'))

    # Given
    pos, acc = run_program_n_times(lines, 8)

    # Then
    assert pos == 1
    assert acc == 5


def test_run_program_n_times_second_star():
    # Given
    lines = clean_lines(read_text_file_lines('test_input_2.txt'))

    # Given
    pos, acc = run_program_n_times(lines, 8)

    # Then
    assert pos == -1
    assert acc == 8


def test_run_program_second_star():
    # Given
    lines = clean_lines(read_text_file_lines('test_input_2.txt'))

    # Given
    pos, acc = run_program(lines)

    # Then
    assert pos == -1
    assert acc == 8


def test_fix_program():
    # Given
    original_program = clean_lines(read_text_file_lines('test_input.txt'))

    # Given
    programs_output = fix_program(original_program)

    # Then

    assert programs_output == [(-1, 8)]
