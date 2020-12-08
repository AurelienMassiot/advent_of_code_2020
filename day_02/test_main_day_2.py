from main_day_2 import split_line, is_password_valid_first_star, is_password_valid_second_star


def test_split_line():
    # Given
    line = '1-3 a: abcde'
    expected_split_line = 1, 3, 'a', 'abcde'

    # When
    actual_split_line = split_line(line)

    # Then
    assert actual_split_line == expected_split_line


def test_is_password_valid_first_star_true():
    # Given
    min_n = 1
    max_n = 3
    letter = 'a'
    password = 'abcde'

    # When
    is_this_password_valid = is_password_valid_first_star(min_n, max_n, letter, password)

    # Then
    assert is_this_password_valid


def test_is_password_valid_first_star_false():
    # Given
    min_n = 1
    max_n = 3
    letter = 'b'
    password = 'cdefg'

    # When
    is_this_password_valid = is_password_valid_first_star(min_n, max_n, letter, password)

    # Then
    assert not is_this_password_valid


def test_is_password_valid_second_star_when_exactly_one_occurrence_true():
    # Given
    min_n = 1
    max_n = 3
    letter = 'a'
    password = 'abcde'

    # When
    is_this_password_valid = is_password_valid_second_star(min_n, max_n, letter, password)

    # Then
    assert is_this_password_valid


def test_is_password_valid_second_star_when_no_occurrence_false():
    # Given
    min_n = 1
    max_n = 3
    letter = 'b'
    password = 'cdefg'

    # When
    is_this_password_valid = is_password_valid_second_star(min_n, max_n, letter, password)

    # Then
    assert not is_this_password_valid


def test_is_password_valid_second_star_when_two_occurrences_false():
    # Given
    min_n = 2
    max_n = 9
    letter = 'c'
    password = 'ccccccccc'

    # When
    is_this_password_valid = is_password_valid_second_star(min_n, max_n, letter, password)

    # Then
    assert not is_this_password_valid
