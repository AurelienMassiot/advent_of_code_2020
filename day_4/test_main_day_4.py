from main_day_4 import is_passport_valid_first_stage, count_valid_passports_first_star, \
    count_valid_passports_second_star, is_hgt_valid, is_hcl_valid, is_ecl_valid


def test_is_password_valid_first_passport_8_fields():
    # Given
    passport = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'

    # When #Then
    assert is_passport_valid_first_stage(passport)


def test_is_password_not_valid_second_passport_missing_height_7_fields():
    # Given
    passport = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'

    # When #Then
    assert not is_passport_valid_first_stage(passport)


def test_is_password_valid_third_passport_missing_cid_passport_7_fields():
    # Given
    passport = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'

    # When #Then
    assert is_passport_valid_first_stage(passport)


def test_is_password_valid_third_missing_cid_passport_7_fields():
    # Given
    passport = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'

    # When #Then
    assert not is_passport_valid_first_stage(passport)


def test_count_passports_on_sample():
    # Give
    filename = 'test_input.txt'
    expected_n = 2

    # When
    n = count_valid_passports_first_star(filename)

    assert n == expected_n


def test_hcl():
    # Give
    hcl_valid_1 = '#123abc'
    hcl_invalid_2 = '#123abz'
    hcl_invalid_3 = '123abc'

    assert is_hcl_valid(hcl_valid_1)
    assert not is_hcl_valid(hcl_invalid_2)
    assert not is_hcl_valid(hcl_invalid_3)


def test_hgt():
    # Give
    hgt_valid_1 = '60in'
    hgt_valid_2 = '190cm'
    hgt_invalid_3 = '190in'
    hgt_invalid_4 = '190'

    assert is_hgt_valid(hgt_valid_1)
    assert is_hgt_valid(hgt_valid_2)
    assert not is_hgt_valid(hgt_invalid_3)
    assert not is_hgt_valid(hgt_invalid_4)


def test_ecl():
    # Give
    hcl_valid_1 = 'brn'
    hcl_invalid_2 = 'wat'

    assert is_ecl_valid(hcl_valid_1)
    assert not is_ecl_valid(hcl_invalid_2)


def test_second_star():
    # Give
    filename = 'test_input.txt'
    expected_n = 2

    # When
    n = count_valid_passports_second_star(filename)

    assert n == expected_n


def test_second_star_invalid_passports():
    # Give
    filename = 'test_invalid_passports.txt'
    expected_n = 0

    # When
    n = count_valid_passports_second_star(filename)

    assert n == expected_n


def test_second_star_valid_passports():
    # Give
    filename = 'test_valid_passports.txt'
    expected_n = 4

    # When
    n = count_valid_passports_second_star(filename)

    assert n == expected_n
