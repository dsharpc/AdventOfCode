import re
from itertools import chain
from random import randint
import time
INPUT_FILE = 'inputs/day16_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.read()
    return data

def range_right(start, stop):
    return range(start, stop+1)

def parse_rules(data):
    bounds = re.findall(r'\d+\-\d+', data)
    bounds = [[int(x) for x in bound.split('-')] for bound in bounds]
    bounds = [range_right(*bound) for bound in bounds]
    bounds = set(chain.from_iterable(bounds))
    return bounds

def parse_nearby_tickets(data):
    tickets = [x.split(',') for x in data.split('nearby tickets:')[1].strip().split('\n')]
    return tickets

def main_part1():
    data = load_data()
    bounds = parse_rules(data)
    nb_tickets = parse_nearby_tickets(data)
    error_rate = 0
    for ticket in nb_tickets:
        for val in ticket:
            val = int(val)
            if val not in bounds:
                error_rate+=val
                break
    print(error_rate)

# main_part1()


def parse_rules_part2(data):
    rdata = data.split('your ticket:')[0].strip().split('\n')
    rulebook = {}
    for i, r in enumerate(rdata):
        name, bounds = r.split(':')
        bounds = re.findall(r'\d+\-\d+', bounds)    
        bounds = [[int(x) for x in bound.split('-')] for bound in bounds]
        bounds = [range_right(*bound) for bound in bounds]
        rulebook[(name,i)] = set(chain.from_iterable(bounds))
    return rulebook

def parse_my_ticket(data):
    tdata = data.split('your ticket:')[1].strip().split('\n')[0].split(',')
    tdata = [int(x) for x in tdata]
    return tdata


def main_part2():
    data = load_data()
    bounds = parse_rules(data)
    nb_tickets = parse_nearby_tickets(data)
    valid_tickets = []
    for ticket in nb_tickets:
        tvals = [int(val) for val in ticket]
        if len(set(tvals)-bounds) > 0:
            continue
        valid_tickets.append(ticket)
    rulebook = parse_rules_part2(data)
    candidate_rules = list(range(len(rulebook)))
    rule_mapping = {}
    cand = 0
    while len(candidate_rules) > 0:
        crule = candidate_rules[cand]
        matches = []
        for rule, bounds in rulebook.items():
            tvals = [int(ticket[crule]) for ticket in valid_tickets]
            if len(set(tvals) - bounds) > 0:
                continue
            matches.append([rule,crule])
        if len(matches) == 1:
            del rulebook[matches[0][0]]
            candidate_rules.remove(matches[0][1])
            rule_mapping[crule] = matches[0][0]
        if len(candidate_rules) > 0:
            cand = (cand+1)% (len(candidate_rules))
    print(rule_mapping)
    my_ticket = parse_my_ticket(data)
    res_sum = 1
    for k,v in rule_mapping.items():
        if 'departure' in v[0]:
            res_sum *= my_ticket[k]
    print(res_sum)

main_part2()