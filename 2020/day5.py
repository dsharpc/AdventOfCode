import re

INPUT_FILE = 'inputs/day5_input.txt'
ROWS = 128
COLUMNS = 8

def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = f.readlines()
    return data

def split_bpass(bpass):
    row = bpass[:7]
    col = bpass[7:]
    return row, col

def recode(row_sequence):
    row_sequence = row_sequence.replace('F','L').replace('B','R')
    return row_sequence

def binary_search(sequence, num_elements):
    value_options = range(num_elements)
    for e in sequence:
        if e == 'L':
            value_options = value_options[:len(value_options)//2]
        elif e == 'R':
            value_options = value_options[len(value_options)//2:]
    return value_options[0]


def main_part_1():
    bpasses = load_data()
    max_id = 0
    for bpass in bpasses:
        row, col = split_bpass(bpass)
        row = recode(row)
        row_num = binary_search(row, ROWS)
        col_num = binary_search(col, COLUMNS)
        seat_id = row_num * 8 + col_num
        if seat_id > max_id:
            max_id = seat_id
    print(max_id)

def find_my_seat(seats):
    seats = sorted(seats)
    for i in range(len(seats)):
        assert seats[i+1] - seats[i] == 1, f"SEAT is between {seats[i]} and {seats[i+1]}"

def main_part_2():
    bpasses = load_data()
    seats = []
    for bpass in bpasses:
        row, col = split_bpass(bpass)
        row = recode(row)
        row_num = binary_search(row, ROWS)
        col_num = binary_search(col, COLUMNS)
        seat_id = row_num * 8 + col_num
        seats.append(seat_id)
    find_my_seat(seats)
    

if __name__=="__main__":
    main_part_2()