from collections import Counter
INPUT_FILE = 'inputs/day2_input.txt'

def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = f.readlines()
    return data

def parse_data(line):
    policy, password = line.split(':')
    rule, required_letter = policy.split()
    mini, maxi = rule.split('-')
    mini = int(mini)
    maxi = int(maxi)
    password = password.strip()
    return mini, maxi, required_letter, password

def validate_password(mini, maxi, req_letter, password):
    counted = Counter(password)
    req_letter_count = counted.get(req_letter, 0)
    if req_letter_count >= mini and req_letter_count <= maxi:
        return True
    else:
        return False

def validate_password_part_2(mini, maxi, req_letter, password):
    exists_in_mini = req_letter in password[mini-1]
    exists_in_maxi = req_letter in password[maxi-1]

    if exists_in_mini + exists_in_maxi == 1:
        return True
    else:
        return False

def main():
    data = load_data()
    valid_passwords = 0
    for line in data:
        res = parse_data(line)
        valid = validate_password_part_2(*res)
        if valid:
            valid_passwords+=1
    print(valid_passwords)


if __name__=="__main__":
    main()
