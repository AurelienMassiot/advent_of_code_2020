import re
from itertools import compress


def read_input(filename):
    with open(filename) as f:
        contents = f.read()
    passports_list = contents.split('\n\n')
    return [passport.replace("\n", " ") for passport in passports_list]


def split_passport(passport):
    return dict(item.split(":") for item in passport.split(" "))


def is_passport_valid_first_stage(passport_dict):
    if all(k in passport_dict for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')):
        return True
    if all(k in passport_dict for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
        return True
    else:
        return False


def count_valid_passports_first_star(filename):
    passports_list = read_input(filename)
    split_passwords_list = [split_passport(passport) for passport in passports_list]
    are_passports_valid = [is_passport_valid_first_stage(passport_dict) for passport_dict in split_passwords_list]
    return sum(are_passports_valid)


def is_hcl_valid(hcl):
    return hcl.startswith('#') and all([c in '0123456789abcdef' for c in hcl[1:]])


def is_ecl_valid(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_hgt_valid(hgt):
    match = re.match(r"([0-9]+)([a-z]+)", hgt, re.I)
    if match:
        items = match.groups()
    else:
        return False

    hgt_number = int(items[0])
    hgt_dimension = items[1]
    return (hgt_number >= 150 and hgt_number <= 193 and hgt_dimension == 'cm') or (
            hgt_number >= 59 and hgt_number <= 76 and hgt_dimension == 'in')


def is_pid_valid(pid):
    return len(pid) == 9


def is_byr_valid(byr):
    return int(byr) >= 1920 and int(byr) <= 2002 and len(byr) == 4


def is_iyr_valid(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020 and len(iyr) == 4


def is_eyr_valid(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030 and len(eyr) == 4


def is_passport_valid_second_stage(passport_dict):
    return is_byr_valid(passport_dict['byr']) \
           and is_iyr_valid(passport_dict['iyr']) \
           and is_eyr_valid(passport_dict['eyr']) \
           and is_hgt_valid(passport_dict['hgt']) \
           and is_hcl_valid(passport_dict['hcl']) \
           and is_ecl_valid(passport_dict['ecl']) \
           and is_pid_valid(passport_dict['pid'])


def count_valid_passports_second_star(filename):
    passports_list = read_input(filename)
    split_passwords_list = [split_passport(passport) for passport in passports_list]
    are_passports_valid = [is_passport_valid_first_stage(passport_dict) for passport_dict in split_passwords_list]
    valid_split_passwords_list_after_stage_1 = list(compress(split_passwords_list, are_passports_valid))
    have_passport_valid_values = [is_passport_valid_second_stage(passport_dict) for passport_dict in
                                  valid_split_passwords_list_after_stage_1]
    return sum(have_passport_valid_values)


def first_star():
    return count_valid_passports_first_star('input.txt')


def second_star():
    return count_valid_passports_second_star('input.txt')


if __name__ == "__main__":
    print(first_star())
    print(second_star())
