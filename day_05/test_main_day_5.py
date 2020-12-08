from main_day_5 import *


def test_get_row():
    # Given
    boarding_pass_1 = "FBFBBFFRLR"
    boarding_pass_2 = "BFFFBBFRRR"
    boarding_pass_3 = "FFFBBBFRRR"
    boarding_pass_4 = "BBFFBBFRLL"

    # When
    row_1 = get_row(boarding_pass_1)
    row_2 = get_row(boarding_pass_2)
    row_3 = get_row(boarding_pass_3)
    row_4 = get_row(boarding_pass_4)

    # Then
    assert row_1 == 44
    assert row_2 == 70
    assert row_3 == 14
    assert row_4 == 102


def test_get_column():
    # Given
    boarding_pass_1 = "FBFBBFFRLR"
    boarding_pass_2 = "BFFFBBFRRR"
    boarding_pass_3 = "FFFBBBFRRR"
    boarding_pass_4 = "BBFFBBFRLL"

    # When
    column_1 = get_column(boarding_pass_1)
    column_2 = get_column(boarding_pass_2)
    column_3 = get_column(boarding_pass_3)
    column_4 = get_column(boarding_pass_4)

    # Then
    assert column_1 == 5
    assert column_2 == 7
    assert column_3 == 7
    assert column_4 == 4


def test_decode_seat_id():
    # Given
    boarding_pass_1 = "FBFBBFFRLR"
    boarding_pass_2 = "BFFFBBFRRR"
    boarding_pass_3 = "FFFBBBFRRR"
    boarding_pass_4 = "BBFFBBFRLL"

    # When
    id_1 = decode_seat_id(boarding_pass_1)
    id_2 = decode_seat_id(boarding_pass_2)
    id_3 = decode_seat_id(boarding_pass_3)
    id_4 = decode_seat_id(boarding_pass_4)

    # Then
    assert id_1 == 357
    assert id_2 == 567
    assert id_3 == 119
    assert id_4 == 820
