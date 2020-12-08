import copy
INPUT_FILE = 'inputs/day8_input.txt'

def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    return data

def parse(data):
    data = [x.split(' ') for x in data]
    return data

def run(data):
    acum = 0
    i = 0
    visited = []
    while True:
        if i in visited:
            break
        if data[i][0] == 'nop':
            visited.append(i)
            i+=1
        elif data[i][0] == 'acc':
            acum+=int(data[i][1])
            visited.append(i)
            i+=1
        elif data[i][0] == 'jmp':
            visited.append(i)
            i+=int(data[i][1])
    return acum


def change_next_value(data_tmp,i):
    for x in range(i, len(data_tmp)):
        if data_tmp[x][0] == 'nop':
            data_tmp[x][0] = 'jmp'
            break
        elif data_tmp[x][0] == 'jmp':
            data_tmp[x][0] = 'nop'
            break
        else:
            continue
    x+=1
    return data_tmp,x

def run_part2(data):
    acum = 0
    i = 0
    visited = []
    while True:
        if i in visited:
            break
        if i >= len(data):
            break
        if data[i][0] == 'nop':
            visited.append(i)
            i+=1
        elif data[i][0] == 'acc':
            acum+=int(data[i][1])
            visited.append(i)
            i+=1
        elif data[i][0] == 'jmp':
            visited.append(i)
            i+=int(data[i][1])
    return acum, i

def main_part_1():
    data = load_data()
    data = parse(data)
    acum = run(data)
    print(acum)

def main_part_2():
    data = load_data()
    data = parse(data)
    i = 0
    while i < len(data):
        data_tmp = copy.deepcopy(data)
        data_tmp, i = change_next_value(data_tmp, i)
        if i > len(data):
            break
        acum, idx = run_part2(data_tmp)
        if idx == len(data):
            break
    print(acum)

if __name__ == "__main__":
    main_part_2()