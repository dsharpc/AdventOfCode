from copy import deepcopy

INPUT_FILE = 'inputs/day11_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    data = [list(x.strip()) for x in data]
    return data


def adjacent_occupied(seats, seat_id):
    ADJACENT_SEATS = [(1,0),(-1,0),(0,1),(0,-1),
                      (1,1),(1,-1),(-1,1),(-1,-1)]
    occupied_seats = 0
    for seat in ADJACENT_SEATS:
        ad_seat_id =tuple([seat_id[0]+seat[0],seat_id[1]+seat[1]])
        if ad_seat_id[0] < 0 or ad_seat_id[1] < 0 or \
           ad_seat_id[0] >= len(seats) or ad_seat_id[1] >= len(seats[0]):
            continue
        if seats[ad_seat_id[0]][ad_seat_id[1]] == '#':
            occupied_seats+=1
    return occupied_seats

def count_occupied(seats):
    occ = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occ+=1
    return occ

def main_part1():
    data = load_data()
    new_map = deepcopy(data)
    while True:
        for i, row in enumerate(data):
            for j, seat in enumerate(row):
                if seat == '.':
                    continue
                elif seat == 'L':
                    occ = adjacent_occupied(data, (i,j))
                    if occ == 0:
                        new_map[i][j] = '#'
                elif seat == '#':
                    occ = adjacent_occupied(data, (i,j))
                    if occ >= 4:
                        new_map[i][j] = 'L'
        if new_map == data:
            break
        else:
            data = deepcopy(new_map)
    occs = count_occupied(data)
    print(occs)


def first_occupied(seats, seat_id):
    ADJACENT_SLOPES = [(1,0),(-1,0),(0,1),(0,-1),
                      (1,1),(1,-1),(-1,1),(-1,-1)]
    occupied_seats = 0
    for slope in ADJACENT_SLOPES:
        ad_seat_id =tuple([seat_id[0]+slope[0],seat_id[1]+slope[1]])
        while True:
            if ad_seat_id[0] < 0 or ad_seat_id[1] < 0 or \
               ad_seat_id[0] >= len(seats) or ad_seat_id[1] >= len(seats[0]):
                break
            if seats[ad_seat_id[0]][ad_seat_id[1]] == 'L':
                break
            if seats[ad_seat_id[0]][ad_seat_id[1]] == '#':
                occupied_seats+=1
                break
            ad_seat_id = tuple([ad_seat_id[0]+slope[0],ad_seat_id[1]+slope[1]])
    return occupied_seats

def main_part2():
    data = load_data()
    new_map = deepcopy(data)
    while True:
        for i, row in enumerate(data):
            for j, seat in enumerate(row):
                if seat == '.':
                    continue
                elif seat == 'L':
                    occ = first_occupied(data, (i,j))
                    if occ == 0:
                        new_map[i][j] = '#'
                elif seat == '#':
                    occ = first_occupied(data, (i,j))
                    if occ >= 5:
                        new_map[i][j] = 'L'
        if new_map == data:
            break
        else:
            data = deepcopy(new_map)
    occs = count_occupied(data)
    print(occs)

main_part2()