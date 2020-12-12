INPUT_FILE = 'inputs/day12_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    return data

def parse_data(data):
    instructions = []
    for el in data:
        ins = (el[0],int(el[1:]))
        instructions.append(ins)
    return instructions

def navigate(instructions):
    map_dir = {'N':(1,0), 'S': (-1,0), 'E':(0,1), 'W': (0,-1)}
    directions = ['E','S','W','N']
    starting_position = (0,0)
    current_position = starting_position
    facing_idx = 0 
    for ins in instructions:
        if ins[0] == 'F':
            facing = directions[facing_idx]
            current_position = tuple([current_position[0]+map_dir[facing][0]*ins[1],
                                     current_position[1]+map_dir[facing][1]*ins[1]])
        elif ins[0] in map_dir:
            current_position = tuple([current_position[0]+map_dir[ins[0]][0]*ins[1],
                                     current_position[1]+map_dir[ins[0]][1]*ins[1]])
        elif ins[0] in ['R','L']:
            if ins[0] == 'R':
                facing_idx = (facing_idx + ins[1]/90) % 4
            if ins[0] == 'L':
                facing_idx = (facing_idx - ins[1]/90) % 4
            facing_idx = int(facing_idx)
    return current_position


def manhattan(final_pos):
    return sum(map(abs, final_pos))

def main_part1():
    data = load_data()
    instructions = parse_data(data)
    pos = navigate(instructions)
    dis = manhattan(pos)
    print(dis)


def rotate_90(position):
    return (-position[1], position[0])

def rotate_m90(position):
    return (position[1], -position[0])

def navigate_waypoint(instructions):
    map_dir = {'N':(1,0), 'S': (-1,0), 'E':(0,1), 'W': (0,-1)}
    current_position = (0,0)
    waypoint_position = (1,10)
    for ins in instructions:
        if ins[0] == 'F':
            current_position = tuple([current_position[0]+waypoint_position[0]*ins[1],
                                     current_position[1]+waypoint_position[1]*ins[1]])
        elif ins[0] in map_dir:
            waypoint_position = tuple([waypoint_position[0]+map_dir[ins[0]][0]*ins[1],
                                     waypoint_position[1]+map_dir[ins[0]][1]*ins[1]])
        elif ins[0] in ['R','L']:
            rots = int(ins[1] / 90) 
            if ins[0] == 'R':
                for _ in range(rots):
                    waypoint_position = rotate_90(waypoint_position)
            else:
                for _ in range(rots):
                    waypoint_position = rotate_m90(waypoint_position)
            
    return current_position

def main_part2():
    data = load_data()
    instructions = parse_data(data)
    pos = navigate_waypoint(instructions)
    dis = manhattan(pos)
    print(dis)

main_part2()

