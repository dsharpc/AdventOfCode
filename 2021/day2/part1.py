
with open('input.txt', 'r') as f:
    input = f.readlines()

horizontal = 0
depth = 0

for line in input:
    direction, value = line.split()
    if direction == "forward":
        horizontal+=int(value)
    elif direction == "down":
        depth+=int(value)
    else:
        depth-=int(value)


print(horizontal * depth)