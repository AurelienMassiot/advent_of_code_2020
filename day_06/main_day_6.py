from collections import Counter


def read_text_file_with_blank_spaces(filename):
    with open(filename) as f:
        contents = f.read()
    passports_list = contents.split('\n\n')
    return [passport.replace("\n", " ") for passport in passports_list]


def count_unique_answers_in_group(answers_in_group):
    return len(set(answers_in_group.replace(' ', '')))


def count_same_answers_in_group(answers_in_group):
    characters_count = Counter(answers_in_group)
    n_same_answers_in_group = 0
    for character in characters_count.keys():
        if character != ' ' and characters_count[character] == (characters_count[' '] + 1):
            n_same_answers_in_group += 1
    return n_same_answers_in_group


def first_star():
    groups_list = read_text_file_with_blank_spaces('input.txt')
    count_unique_answers = [count_unique_answers_in_group(answers_in_group) for answers_in_group in groups_list]
    return sum(count_unique_answers)


def second_star():
    groups_list = read_text_file_with_blank_spaces('input.txt')
    count_same_answers = [count_same_answers_in_group(answers_in_group) for answers_in_group in groups_list]
    return sum(count_same_answers)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
