from collections import defaultdict

with open('input.txt', 'r') as f:
    input = f.read().split(',')

lanternfish = defaultdict(int)

for x in input:
    lanternfish[int(x)]+=1

NUM_DAYS = 256

day=0
while day < NUM_DAYS:
    old_fish = lanternfish[0]
    for i in range(0, 8):
        lanternfish[i] = lanternfish[i+1]
    lanternfish[8] = old_fish
    lanternfish[6] += old_fish
    day+=1
print(sum(lanternfish.values()))
    