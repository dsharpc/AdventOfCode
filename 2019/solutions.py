
def day_1():
    with open('inputs/day1.txt') as f:
        data = f.read()

    data = data.split('\n')[:-1]

    data = [int(x) for x in data]

    processed = [int(x/3)-2 for x in data]
    print(sum(processed))


def calculate_fuel(mass):
    fuel = int(mass/3)-2
    fuel = 0 if fuel < 0 else fuel
    return fuel


def day_1b():
    with open('inputs/day1.txt') as f:
        data = f.read()

    data = data.split('\n')[:-1]

    data = [int(x) for x in data]

    fuels = []

    for module in data:
        fuel = calculate_fuel(module)
        fuels.append(fuel)
        while fuel > 0:
            fuel = calculate_fuel(fuel)
            fuels.append(fuel)

    print(sum(fuels))


def day_2():
    with open('inputs/day2.txt') as f:
        data = f.read()
        data = data.split(',')
        data = [int(x) for x in data]

    data[1] = 12
    data[2] = 2
    i=0
    while i <= len(data):
        el = data[i]
        if el == 99:
            break
        elif el == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif el == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            print('Unknown code')
        i+=4
    print(data[0])


def calculate(noun, verb):
    with open('inputs/day2.txt') as f:
        data = f.read()
        data = data.split(',')
        data = [int(x) for x in data]

    data[1] = noun
    data[2] = verb
    i=0
    while i <= len(data):
        el = data[i]
        if el == 99:
            break
        elif el == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif el == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            print('Unknown code')
        i+=4
    return(data[0])


def day_2b():
    nouns = range(99)
    verbs = range(99)

    output = 0
    for noun in nouns:
        for verb in verbs:
            output = calculate(noun, verb)
            if output == 19690720:
                print('n: ',noun)
                print('v: ',verb)
                break
            else:
                continue
            break


def calculate_path(path, full_path):
    for step in path:
        if step[0] == 'U':
            for _ in range(int(step[1:])):
                full_path.append((full_path[-1][0]+1,full_path[-1][1]))
        elif step[0] == 'D':
            for _ in range(int(step[1:])):
                full_path.append((full_path[-1][0]-1, full_path[-1][1]))  
        elif step[0] == 'R':
            for _ in range(int(step[1:])):
                full_path.append((full_path[-1][0], full_path[-1][1]+1))
        elif step[0] == 'L':
            for _ in range(int(step[1:])):
                full_path.append((full_path[-1][0], full_path[-1][1]-1))   
    return full_path


def day_3():
    with open('inputs/day3.txt') as f:
        data = f.read()
        path1= data.split('\n')[0]
        path2 = data.split('\n')[1]
        path1 = path1.split(',')
        path2 = path2.split(',')

        start_position = (0,0)
        full_path1 = [start_position]
        full_path2 = [start_position]
        
        full_path1 = calculate_path(path1, full_path1)
        full_path2 = calculate_path(path2, full_path2)
    print(len(full_path1))
    print(len(full_path2))
    print('Will cross')
    crosses = set(full_path1).intersection(full_path2)
    print('crossed')
    distance = []
    steps = []
    for cross in crosses:
        if cross != (0,0):
            distance.append(abs(cross[0]) + abs(cross[1]))
            print(cross, 'distance is', abs(cross[0]) + abs(cross[1]))
            steps.append(full_path1.index(cross) + full_path2.index(cross))
            print(full_path1.index(cross), '-' , full_path2.index(cross), '=', full_path1.index(cross) + full_path2.index(cross))
    print('Part A: The min distance is: ', min(distance))
    print('Part B: The min steps are: ', min(steps))


def day_4():
    num_pass = 0
    range_nums = list(range(231832,767346))
    for i in range_nums:
        c1 = False
        c2 = True
        for ind, dig in enumerate(str(i)):
            if ind+1 < len(str(i)):
                if int(dig) == int(str(i)[ind+1]):
                    c1 = True
                if int(dig) > int(str(i)[ind+1]):
                    c2 = False
                    break
        if c1 and c2:
            num_pass +=1

    print(num_pass)


def day_4b():
    num_pass = 0
    range_nums = list(range(231832,767346))
    for i in range_nums:
        c1 = False
        c2 = True
        min_rep = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for ind, dig in enumerate(str(i)):
            if ind+1 < len(str(i)):
                if int(dig) == int(str(i)[ind+1]):
                    min_rep[int(dig)]+=1
                if int(dig) > int(str(i)[ind+1]):
                    c2 = False
                    break
        try:
            val = sorted(set(min_rep.values()))[1]
        except IndexError:
            val = 0
        if  val == 1:
            c1=True
        if c1 and c2:
            print(i, '-', c1, '-',c2, '-', min_rep)
            num_pass +=1

    print(num_pass)



def day_5():
    with open('inputs/day5.txt') as f:
        data = f.read()
        data = data.split(',')
        data = [int(x) for x in data]

    i=0
    while i <= len(data):
        el = data[i]
        if len(str(el)) == 4:
            instruction = int(str(lol)[2:])
            
        if el == 99:
            break
        elif el == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            i+=4
        elif el == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            i+=4
        elif el == 3:
            data[data[i+1]] = input('Insert value\n')
            i+=2
        elif el == 4:
            print(data[data[i+1]])
            i+=2
        else:
            print('Unknown code')
        
    return(data[0])


