from collections import defaultdict, Counter, deque
from functools import partial
import time
INPUT_FILE = 'inputs/day15_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.read()
    data = [int(x) for x in data.split(',')]
    return data

def play_game(numbers):
    turn = len(numbers)
    memory = defaultdict(partial(deque, maxlen=2))
    for i, num in enumerate(numbers):
        memory[num].append(i+1)
    last_num = numbers[-1]
    while True:
        st = time.time()
        turn +=1
        if len(memory[last_num]) == 1:
            last_num = 0
            memory[last_num].append(turn)
        else:        
            last_num = memory[last_num][1] - memory[last_num][0]
            memory[last_num].append(turn)
        if turn == 30000000:
            return last_num
        if turn % 1000000 == 0:
            print("Turn number: ",turn)
            print("Exec time: ", time.time() - st)

def main_part1():
    numbers = load_data()
    res = play_game(numbers)
    print(res)

main_part1()

