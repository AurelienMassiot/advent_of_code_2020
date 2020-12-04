from main_day_4 import is_passport_valid, read_input, count_valid_passports


def test_is_password_valid_first_passport_8_fields():
    # Given
    passport = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'

    # When #Then
    assert is_passport_valid(passport)

def test_is_password_not_valid_second_passport_missing_height_7_fields():
    # Given
    passport = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'

    # When #Then
    assert not is_passport_valid(passport)

def test_is_password_valid_third_passport_missing_cid_passport_7_fields():
    # Given
    passport = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'

    # When #Then
    assert is_passport_valid(passport)

def test_is_password_valid_third_missing_cid_passport_7_fields():
    # Given
    passport = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'

    # When #Then
    assert not is_passport_valid(passport)

def test_count_passports_on_sample():
    # Give
    filename = 'test_input.txt'
    expected_n = 2

    # When
    n = count_valid_passports(filename)

    assert n == expected_n

