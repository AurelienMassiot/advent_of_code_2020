def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def is_valid_sum(n_list, index, preamble_number):
    for first_cursor in range(index - preamble_number, index - 1):
        for second_cursor in range(index - preamble_number + 1, index):
            if n_list[first_cursor] + n_list[second_cursor] == n_list[index]:
                return True
    return False


def find_incorrect_number(n_list, preamble_number):
    for index in range(preamble_number, len(n_list)):
        if not is_valid_sum(n_list, index, preamble_number):
            return n_list[index]


def find_encryption_weakness(n_list, invalid_number):
    for i, current_n in enumerate(n_list):
        accumulator = [current_n]
        for next_n in n_list[i + 1:]:
            accumulator.append(next_n)
            accumulator_sum = sum(accumulator)
            if accumulator_sum == invalid_number:
                return min(accumulator) + max(accumulator)
            if accumulator_sum > invalid_number:
                break


def first_star():
    preamble_number = 25
    n_list = read_text_file_lines('input.txt')
    return find_incorrect_number(n_list, preamble_number)


def second_star():
    n_list = read_text_file_lines('input.txt')
    invalid_number = first_star()
    encryption_weakness = find_encryption_weakness(n_list, invalid_number)
    return encryption_weakness


if __name__ == "__main__":
    print(first_star())
    print(second_star())
