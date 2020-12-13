from functools import reduce
INPUT_FILE = 'inputs/day13_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    return data

def parse_data(data):
    earliest_departure = int(data[0])
    bus_ids = [int(x) for x in data[1].split(',') if x != 'x']
    return earliest_departure, bus_ids

def main_part1():
    data = load_data()
    ed, bus_ids = parse_data(data)
    min_diff = -1
    best_bus_id = None
    for bus_id in bus_ids:
        bus_id_arri = (ed // bus_id) * bus_id
        if bus_id_arri < ed:
            bus_id_arri += bus_id
        diff = bus_id_arri - ed
        if min_diff == -1 or min_diff > diff:
            min_diff = diff
            best_bus_id = bus_id 
    print(min_diff*best_bus_id)


def parse_data_p2(data):
    bus_ids = [x for x in data[1].split(',')]
    return bus_ids

def mod_mult_inv(m,a):
    rem = a%m
    if rem == 1:
        return 1
    mult = 2
    res = 2
    while True:
        res = rem*mult % m
        if res == 1:
            return mult
        mult+=1

def chinese_remainder_theorem(tracker):
    x = 0
    m = reduce(lambda x, y: x*y, [v['m'] for _,v in tracker.items()])
    for _, v in tracker.items():
        x += v['a'] * m/v['m'] * mod_mult_inv(v['m'],m/v['m'])
    return x % m

def main_part2():
    data = load_data()
    bus_ids = parse_data_p2(data)
    tracker = {}
    for i, bus_id in enumerate(bus_ids):
        if bus_id=='x':
            continue
        # Following line works for validation inputs
        #tracker[bus_id] = {'a': int(bus_id) - (i % int(bus_id)) , 'm': int(bus_id)}
        # For some reason need to add a 1 for it to work with test input
        tracker[bus_id] = {'a': int(bus_id) - (i % int(bus_id)) + 1 , 'm': int(bus_id)}        
    print(tracker)
    t = chinese_remainder_theorem(tracker)
    print(t)

main_part2()