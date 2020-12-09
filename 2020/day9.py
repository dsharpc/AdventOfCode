INPUT_FILE = 'inputs/day9_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    return data


def find_sum(data, target):
    data = list(set(data.copy()))
    for i in range(len(data)):
        for k in range(i, len(data)):
            if data[i] + data[k] == target:
                return True
    return False


def find_not_sum(data, window=25):
    for i in range(window, len(data)-1):
        found = find_sum(data[i-window:i], data[i])
        if not found:
            return data[i]

def main_part1():
    data = load_data()
    found = find_not_sum(data, window=25)
    print(found)

def find_contiguous_sum(data, target):
    for i in range(len(data)):
        for j in range(len(data)):
            if sum(data[i:j]) == target:
                return max(data[i:j]) + min(data[i:j])

def main_part2():
    data = load_data()
    found = find_contiguous_sum(data, 20874512)
    print(found)

main_part2()