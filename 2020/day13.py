import math
INPUT_FILE = 'inputs/test_day13_input.txt'


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

def find_t(tracker):
    maxim = max(tracker.items(), key = lambda x: x[1]['depart'])[0]
    itern = 0
    x = 1
    while True:
        t = tracker[maxim]['depart']*x - tracker[maxim]['offset']
        mods = 0
        for key in tracker.keys():
            if key == maxim:
                continue
            mod = (t + tracker[key]['offset']) % tracker[key]['depart']
            if mod > 0:
                mods+=1
                break
        if mods == 0:
            return t
        
        x+=1
        itern+=1

def main_part2():
    data = load_data()
    bus_ids = parse_data_p2(data)
    tracker = {}
    for i, bus_id in enumerate(bus_ids):
        if bus_id=='x':
            continue
        tracker[bus_id] = {'offset': i, 'depart': int(bus_id)}

    t = find_t(tracker)
    print(t)

main_part2()