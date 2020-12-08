
from main_day_8 import *

def test_process_instruction():
    # Given
    instruction_1 = ('nop', +0)
    instruction_2 = ('acc', +3)
    instruction_3 = ('jmp', +3)
    instruction_4 = ('jmp', -1)

    # Given
    assert process_instruction(instruction_1, pos=0, acc=0) == (1, 0)
    assert process_instruction(instruction_2, pos=0, acc=0) == (1, 3)
    assert process_instruction(instruction_3, pos=0, acc=0) == (3, 0)
    assert process_instruction(instruction_4, pos=1, acc=0) == (0, 0)


def test_input():
    # Given
    lines = clean_lines(read_text_file_lines('test_input.txt'))

    # Given
    pos, acc = run_program(lines)

    # Then
    assert pos == 1
    assert acc == 5
