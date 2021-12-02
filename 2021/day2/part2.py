
with open('input.txt', 'r') as f:
    input = f.readlines()

horizontal = 0
depth = 0
aim = 0

for line in input:
    direction, value = line.split()
    value = int(value)
    if direction == "forward":
        horizontal+=value
        depth+=aim*value
    elif direction == "down":
        aim+=value
    else:
        aim-=value


print(horizontal * depth)