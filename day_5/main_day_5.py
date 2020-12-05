def read_text_file_lines(input_file_path):
    with open(input_file_path, 'r') as input_file:
        return [str(line) for line in input_file.read().splitlines()]


def binary_to_int(row_binary):
    return int(row_binary, base=2)


def get_row(seat):
    row_binary = seat[:-3].replace('F', '0').replace('B', '1')
    return binary_to_int(row_binary)


def get_column(seat):
    column_binary = seat[-3:].replace('L', '0').replace('R', '1')
    return binary_to_int(column_binary)


def decode_seat_id(seat):
    return get_row(seat) * 8 + get_column(seat)


def get_max_id(seat_id_list):
    return max(seat_id_list)


def first_star():
    boarding_pass_list = read_text_file_lines('input.txt')
    seat_id_list = [decode_seat_id(seat) for seat in boarding_pass_list]
    return get_max_id(seat_id_list)


def find_missing_ids(seat_id_list):
    return [seat_id for seat_id in range(0, get_max_id(seat_id_list)) if
            seat_id not in seat_id_list and seat_id + 1 in seat_id_list and seat_id - 1 in seat_id_list
            ]


def second_star():
    boarding_pass_list = read_text_file_lines('input.txt')
    seat_id_list = [decode_seat_id(seat) for seat in boarding_pass_list]
    return find_missing_ids(seat_id_list)


if __name__ == "__main__":
    print(first_star())
    print(second_star())
