import statistics
import math

with open('input.txt', 'r') as f:
    input = f.read().split(',')

positions = [int(x) for x in input]

mean = statistics.mean(positions)

mean = math.floor(mean)

fuel = 0

for pos in positions:
    for f in range(1, abs(pos-int(mean))+1):
        fuel+=f
print(fuel)