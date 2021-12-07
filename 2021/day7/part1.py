import statistics

with open('input.txt', 'r') as f:
    input = f.read().split(',')

positions = [int(x) for x in input]

median = statistics.median(positions)

fuel = 0

for pos in positions:
    fuel += abs(int(pos-median))

print(fuel)