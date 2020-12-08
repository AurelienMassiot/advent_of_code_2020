def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def clean_lines(lines):
    splitted_lines = [line.split(' ') for line in lines]
    return splitted_lines


def process_instruction(instruction, pos, acc):
    cmd = instruction[0]
    n = int(instruction[1])
    if cmd == 'nop':
        return pos + 1, acc
    elif cmd == 'acc':
        return pos + 1, acc + n
    elif cmd == 'jmp':
        return pos + n, acc


def run_program(lines):
    pos = 0
    acc = 0
    visited = {}
    while True:
        instruction = lines[pos]
        pos, acc = process_instruction(instruction, pos, acc)
        if pos in visited:
            break
        visited[pos] = 'visited'
    return pos, acc


def first_star():
    lines = clean_lines(read_text_file_lines('input.txt'))
    pos, acc = run_program(lines)
    return pos, acc


def second_star():
    pass


if __name__ == "__main__":
    print(first_star())
    print(second_star())
