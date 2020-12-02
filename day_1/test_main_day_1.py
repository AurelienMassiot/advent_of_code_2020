from main import select_the_two_entries, select_the_three_entries


def test_select_two_entries_in_example_when_one_entry_is_first():
    # Given
    expense_report = [1721, 979, 366, 299, 675, 1456]
    expected_two_entries = 1721, 299

    # When
    actual = select_the_two_entries(expense_report)

    # Then
    assert actual == expected_two_entries


def test_select_two_entries_in_example_when_one_entry_is_not_first():
    # Given
    expense_report = [979, 1721, 366, 299, 675, 1456]
    expected_two_entries = 1721, 299

    # When
    actual = select_the_two_entries(expense_report)

    # Then
    assert actual == expected_two_entries


def test_select_three_entries_in_example_when_one_entry_is_first():
    # Given
    expense_report = [979, 1721, 366, 299, 675, 1456]
    expected_three_entries = 979, 366, 675

    # When
    actual = select_the_three_entries(expense_report)

    # Then
    assert actual == expected_three_entries


def test_select_three_entries_in_example_when_one_entry_is_not_first():
    # Given
    expense_report = [1721, 979, 366, 299, 675, 1456]
    expected_three_entries = 979, 366, 675

    # When
    actual = select_the_three_entries(expense_report)

    # Then
    assert actual == expected_three_entries
