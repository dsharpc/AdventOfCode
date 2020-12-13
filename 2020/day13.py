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

def check_same_depart(tracker):
    vals = [x['depart'] - x['offset'] for x in tracker.values()]
    mvals = max(vals)
    if len(set(vals))==1:
        return True
    else:
        return False


def main_part2():
    data = load_data()
    bus_ids = parse_data_p2(data)
    tracker = {}
    for i, bus_id in enumerate(bus_ids):
        if bus_id=='x':
            continue
        tracker[bus_id] = {'offset': i, 'depart': int(bus_id)}

    while True:
        same = check_same_depart(tracker)
        if same:
            break
        lowest = min(tracker.items(), key=lambda x: x[1].get('depart'))[0]
        tracker[lowest]['depart'] += int(lowest)
    print([v['depart'] for k,v in tracker.items() if v['offset'] == 0])

main_part2()