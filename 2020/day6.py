from collections import Counter

INPUT_FILE = 'inputs/day6_input.txt'

def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = f.read()
    return data

def get_questionnaire(data):
    ques = data.split('\n\n')
    return ques

def get_num_questions(ques):
    ques = ques.replace('\n','').strip()
    num = set(ques)
    return len(num) 

def get_num_questions_all(ques):
    keys = 0
    num_users = len(ques.split('\n'))
    ques = ques.replace('\n','').strip()
    counted = Counter(ques)
    for k, v in counted.items():
        if v == num_users:
            keys+=1
    return keys

def main_part1():
    data = load_data()
    quess = get_questionnaire(data)
    num_questions = 0
    for ques in quess:
        num_questions += get_num_questions(ques)
    print(num_questions)

def main_part2():
    data = load_data()
    quess = get_questionnaire(data)
    num_questions = 0
    for ques in quess:
        num_questions += get_num_questions_all(ques)
    print(num_questions)

main_part2()