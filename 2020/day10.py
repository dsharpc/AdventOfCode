INPUT_FILE = 'inputs/day10_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    return data

def connect_adapters(data):
    data = sorted(data)
    last_joltage = 0
    jump1 = 0
    jump3 = 1
    for ad in data:
        jump = ad - last_joltage
        if jump == 1:
            jump1+=1
        elif jump == 3:
            jump3+=1
        last_joltage = ad
    return jump1 * jump3

def main_part1():
    data = load_data()
    res = connect_adapters(data)
    print(res)



def try_new(data, used_adapters = [0], candidate_conn={}):
    num_connections = 0
    candidates = list(filter(lambda x: (used_adapters[-1]) < x <= (used_adapters[-1] + 3), data))
    if len(candidates) == 1:
        if candidates[0] == max(data):
            return 1
    for ad in candidates:
        if ad in candidate_conn:
            num_connections += candidate_conn[ad]
        else:
            try_adapters = used_adapters + [ad]
            conns = try_new(data, try_adapters, candidate_conn)
            candidate_conn[ad] = conns
            num_connections+=conns
    return num_connections

def main_part2():
    data = load_data()
    data.append(max(data)+3)
    num_conn = try_new(data)
    print(num_conn)

main_part2()