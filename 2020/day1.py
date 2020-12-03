INPUT_FILE = 'inputs/day1_input.txt'


def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = f.readlines()
    data = [int(x) for x in data]
    return data

def find_nums(data):
    data = sorted(data)
    for i in range(len(data)):
        for j in range(i,len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def find_nums_part_2(data):
    data = sorted(data)
    for i in range(len(data)):
        for j in range(i,len(data)):
            for k in range(j,len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

def main():
    data = load_data()
    mult = find_nums_part_2(data)
    print(mult)


if __name__ == "__main__":
    main()