ALL_PASSWORD_KEYS = {""}

def read_input(filename):
    with open(filename) as f:
        contents = f.read()
    passports_list = contents.split('\n\n')
    return [passport.replace("\n"," ") for passport in passports_list]


def is_passport_valid(passport):

    password_dict = split_passport(passport)
    if all (k in password_dict for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')):
        return True
    if all(k in password_dict for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
        return True
    else:
        return False


def split_passport(passport):
    print(passport)
    return dict(item.split(":") for item in passport.split(" "))


def count_valid_passports(filename):
    passports_list = read_input(filename)
    are_passports_valid = [is_passport_valid(passport) for passport in passports_list]
    return sum(are_passports_valid)

def first_star():
    return count_valid_passports('input.txt')


def second_star():
    pass


if __name__ == "__main__":
    print(first_star())
    print(second_star())
