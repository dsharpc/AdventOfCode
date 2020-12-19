from copy import deepcopy
INPUT_FILE = 'inputs/day17_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    data = [list(x.strip()) for x in data]
    return data

def make_3d(data):
    out_data = [] 
    dim = len(data)
    row = list(dim * '.')
    layer =[deepcopy(row) for x in range(dim)]
    out_data.append(deepcopy(layer))
    out_data.append(deepcopy(data))
    out_data.append(deepcopy(layer))
    return out_data

def expand_dimension(data):
    data = deepcopy(data)
    dim = len(data[0])
    data.insert(0, [list(dim*'.') for x in range(dim)])
    data.append([list(dim*'.') for x in range(dim)])
    for i, layer in enumerate(data):
        data[i].insert(0, list(dim * '.'))
        data[i].append(list(dim * '.'))
    for i, layer in enumerate(data):
        for j, row in enumerate(layer):
            data[i][j].insert(0,'.')
            data[i][j].append('.')
    return data



def gen_adjacent_cubes(mask=['X','X','X'], i=0, running_mask='',masks = []):
    mask = mask.copy()
    if i == len(mask):
        masks.append(running_mask)
    elif mask[i] == 'X':
        mask_1 = mask
        mask_1[i] = '1'
        gen_adjacent_cubes(mask_1, i, running_mask, masks)
        mask_0 = mask
        mask_0[i] = '0'
        gen_adjacent_cubes(mask_0, i, running_mask, masks)
        mask_m1 = mask
        mask_m1[i] = '2'
        gen_adjacent_cubes(mask_m1, i, running_mask, masks)
    else:
        running_mask+=mask[i]
        i+=1
        gen_adjacent_cubes(mask, i, running_mask, masks)

    return masks

def format_adjacency(adj):
    adjacents = []
    for ad in adj:
        if ad == '000':
            continue
        adjacents.append([int(x) if x != '2' else -1 for x in ad])
    return adjacents

def adjacent_active(cubes, cube_pos, adj):
    ADJACENT_CUBES = adj
    active_cubes = 0
    for cube in ADJACENT_CUBES:
        ad_cube_id =tuple([cube_pos[0]+cube[0],cube_pos[1]+cube[1],cube_pos[2]+cube[2]])
        if ad_cube_id[0] < 0 or ad_cube_id[1] < 0 or ad_cube_id[2] < 0 or\
           ad_cube_id[0] >= len(cubes) or ad_cube_id[1] >= len(cubes[0]) or\
               ad_cube_id[2] >= len(cubes[0]):
            continue
        if cubes[ad_cube_id[0]][ad_cube_id[1]][ad_cube_id[2]] == '#':
            active_cubes+=1
    return active_cubes


def count_active(cubes):
    occ = 0
    for layer in cubes:
        for row in layer:
            for cube in row:
                if cube == '#':
                    occ+=1
    return occ

def print_cubes(cubes):
    for i in range(len(cubes)):
        print('\nz = ',i-1)
        for row in cubes[i]:
            print(''.join(row))

def main_part1():
    data = load_data()
    data = make_3d(data)
    adj = gen_adjacent_cubes()
    adj = format_adjacency(adj)
    new_cubes = deepcopy(data)
    for _ in range(6):
        data = expand_dimension(new_cubes)
        new_cubes = deepcopy(data)
        for i, layer in enumerate(data):
            for j, row in enumerate(layer):
                for k, cube in enumerate(row):
                    if cube == '#':
                        occ = adjacent_active(data, (i,j,k), adj)
                        if occ not in (2,3):
                            new_cubes[i][j][k] = '.'
                    elif cube == '.':
                        occ = adjacent_active(data, (i,j,k), adj)
                        if occ == 3:
                            new_cubes[i][j][k] = '#'
        print(f'\ncube in {i},{j},{k}')
        print(f"Active neighbour cubes = {occ}")
        print_cubes(new_cubes)
    active = count_active(new_cubes)
    print_cubes(new_cubes)
    print(active)
    
main_part1()