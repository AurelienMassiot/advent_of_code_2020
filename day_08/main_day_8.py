import copy


def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def clean_lines(lines):
    splitted_lines = [line.split(' ') for line in lines]
    return splitted_lines


def process_instruction(instruction, pos, acc, n_max_lines):
    cmd = instruction[0]
    n = int(instruction[1])
    if cmd == 'nop':
        return pos + 1, acc
    elif cmd == 'acc':
        if pos + 1 >= n_max_lines:
            return -1, acc + n
        else:
            return pos + 1, acc + n
    elif cmd == 'jmp':
        return pos + n, acc


def run_program(lines):
    pos = 0
    acc = 0
    visited = {}
    n_max_lines = len(lines) - 1
    while True:
        instruction = lines[pos]
        pos, acc = process_instruction(instruction, pos, acc, n_max_lines)
        if pos in visited or pos == -1:
            break
        visited[pos] = 'visited'
    return pos, acc


def run_program_n_times(lines, n):
    n_max_lines = len(lines)
    pos = 0
    acc = 0
    visited = {}
    for i in range(1, n):
        instruction = lines[pos]
        pos, acc = process_instruction(instruction, pos, acc, n_max_lines)
        visited[pos] = 'visited'
        if pos == -1:
            break
    return pos, acc


def create_new_program(i, original_program):
    new_program = copy.deepcopy(original_program)
    if new_program[i][0] == 'nop':
        new_program[i][0] = new_program[i][0].replace('nop', 'jmp')
    elif new_program[i][0] == 'jmp':
        new_program[i][0] = new_program[i][0].replace('jmp', 'nop')
    return new_program


def fix_program(original_program):
    programs_output = []
    for i in range(len(original_program)):
        new_program = create_new_program(i, original_program)
        if new_program == original_program:
            continue
        pos, acc = run_program(new_program)
        if pos == -1 and acc > 0:
            programs_output.append((pos, acc))
    return programs_output


def first_star():
    original_program = clean_lines(read_text_file_lines('input.txt'))
    pos, acc = run_program(original_program)
    return pos, acc


def second_star():
    original_program = clean_lines(read_text_file_lines('input.txt'))
    programs_output = fix_program(original_program)
    return programs_output


if __name__ == "__main__":
    print(first_star())
    print(second_star())
