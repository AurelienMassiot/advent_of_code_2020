from main_day_6 import *


def test_count_unique_answers_in_group():
    # Given
    answers_group_1 = "abc"
    answers_group_2 = "a b c"
    answers_group_3 = "ab ac"
    answers_group_4 = "a a a a"
    answers_group_5 = "b"

    # When
    n_unique_answers_group_1 = count_unique_answers_in_group(answers_group_1)
    n_unique_answers_group_2 = count_unique_answers_in_group(answers_group_2)
    n_unique_answers_group_3 = count_unique_answers_in_group(answers_group_3)
    n_unique_answers_group_4 = count_unique_answers_in_group(answers_group_4)
    n_unique_answers_group_5 = count_unique_answers_in_group(answers_group_5)

    # Then
    assert n_unique_answers_group_1 == 3
    assert n_unique_answers_group_2 == 3
    assert n_unique_answers_group_3 == 3
    assert n_unique_answers_group_4 == 1
    assert n_unique_answers_group_5 == 1


def test_count_same_answers_in_group():
    # Given
    answers_group_1 = "abc"
    answers_group_2 = "a b c"
    answers_group_3 = "ab ac"
    answers_group_4 = "a a a a"
    answers_group_5 = "b"

    # When
    n_same_answers_group_1 = count_same_answers_in_group(answers_group_1)
    n_same_answers_group_2 = count_same_answers_in_group(answers_group_2)
    n_same_answers_group_3 = count_same_answers_in_group(answers_group_3)
    n_same_answers_group_4 = count_same_answers_in_group(answers_group_4)
    n_same_answers_group_5 = count_same_answers_in_group(answers_group_5)

    # Then
    assert n_same_answers_group_1 == 3
    assert n_same_answers_group_2 == 0
    assert n_same_answers_group_3 == 1
    assert n_same_answers_group_4 == 1
    assert n_same_answers_group_5 == 1
