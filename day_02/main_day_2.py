def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def split_line(line):
    tokens = line.split(' ')
    min_n = int(tokens[0].split('-')[0])
    max_n = int(tokens[0].split('-')[1])
    letter = tokens[1][0]
    password = tokens[2]
    return min_n, max_n, letter, password


def is_password_valid_first_star(min_n, max_n, letter, password):
    n_occurrences = password.count(letter)
    return True if n_occurrences >= min_n and n_occurrences <= max_n else False


def is_password_valid_second_star(min_n, max_n, letter, password):
    n_position_1 = 1 if password[min_n - 1] == letter else 0
    n_position_2 = 1 if password[max_n - 1] == letter else 0
    n_positions = n_position_1 + n_position_2
    return True if n_positions == 1 else False


def first_star():
    entries_list = read_input('input.txt')
    split_entries_list = [split_line(line) for line in entries_list]
    are_passwords_valid_list = [is_password_valid_first_star(split_line[0], split_line[1], split_line[2], split_line[3])
                                for
                                split_line in split_entries_list]
    return sum(are_passwords_valid_list)


def second_star():
    entries_list = read_input('input.txt')
    split_entries_list = [split_line(line) for line in entries_list]
    are_passwords_valid_list = [
        is_password_valid_second_star(split_line[0], split_line[1], split_line[2], split_line[3])
        for
        split_line in split_entries_list]
    return sum(are_passwords_valid_list)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
