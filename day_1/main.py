def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def convert_list_str_to_int(list_str):
    return list(map(int, list_str))


def select_the_two_entries(expense_report):
    for first_number in expense_report:
        for second_number in expense_report[1:]:
            if (first_number + second_number) == 2020:
                return first_number, second_number
            else:
                pass


def select_the_three_entries(expense_report):
    for first_number in expense_report:
        for second_number in expense_report[1:]:
            for third_number in expense_report[2:]:
                if (first_number + second_number + third_number) == 2020:
                    return first_number, second_number, third_number
                else:
                    pass


def first_star():
    expense_report = convert_list_str_to_int(read_input('input.txt'))
    first_entry, second_entry = select_the_two_entries(expense_report)
    print(first_entry, second_entry, first_entry * second_entry)


def second_star():
    expense_report = convert_list_str_to_int(read_input('input.txt'))
    first_entry, second_entry, third_entry = select_the_three_entries(expense_report)
    print(first_entry, second_entry, third_entry, first_entry * second_entry * third_entry)


if __name__ == "__main__":
    first_star()
    second_star()
