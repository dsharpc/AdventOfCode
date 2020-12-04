import re

INPUT_FILE = 'inputs/day4_input.txt'

def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = f.read()
    return data

def get_passports(data):
    passports = data.split('\n\n')
    return passports

def clean_passport(passport):
    dictio = {}
    passport = passport.replace('\n',' ')
    keyvalues = passport.split()
    for keyvalue in keyvalues:
        key, value = keyvalue.split(':')
        dictio[key] = value
    return dictio

def validate_passport(passport):
    REQUIRED_KEYS = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for key in REQUIRED_KEYS:
        if key not in passport.keys():
            return 0
    return 1

def validate_passport_keys(passport):
    try:
        assert 1920 <= int(passport['byr']) <= 2002
        assert 2010 <= int(passport['iyr']) <= 2020
        assert 2020 <= int(passport['eyr']) <= 2030
        if 'cm' in passport['hgt']:
            height = passport['hgt'].replace('cm','')
            assert 150 <= int(height) <= 193
        elif 'in' in passport['hgt']:
            height = passport['hgt'].replace('in','')
            assert 59 <= int(height) <= 76
        else:
            assert 1 == 0
        hair_color = re.search(r'^#[0-9a-f]{6}$', passport['hcl'])
        assert hair_color is not None
        assert passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
        passport_id = re.search(r'^[0-9]{9}$', passport['pid'])
        assert passport_id is not None
    except:
        return 0
    return 1


def main_part1():
    data = load_data()
    passports = get_passports(data)
    valid_passports = 0
    for passport in passports:
        dictio = clean_passport(passport)
        valid_passports += validate_passport(dictio)
    print(valid_passports)

def main_part2():
    data = load_data()
    passports = get_passports(data)
    valid_passports = 0
    for passport in passports:
        dictio = clean_passport(passport)
        validity = validate_passport(dictio)
        if validity == 1:
            valid_passports += validate_passport_keys(dictio)
    print(valid_passports)

if __name__=="__main__":
    main_part2()
    