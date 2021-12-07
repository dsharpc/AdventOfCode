with open('input.txt', 'r') as f:
    input = f.read().splitlines()

vent_lines = []
for line in input:
    start, end = line.split('->')
    x1, y1 = start.split(',')
    x2, y2 = end.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1 == x2 or y1 == y2:
        if x2 < x1 or y2 < y1:
            vent_lines.append([(x2,y2), (x1,y1)])
        else:
            vent_lines.append([(x1,y1), (x2,y2)])

rows = 1000
columns = 1000

overlapping_point=0
ocean_floor = [[0 for _ in range(rows)] for _ in range(columns)]

for start, end in vent_lines:
    # Horizontal lines
    ux1=start[1]
    uy1=start[0]
    if start[1] == end[1]:
        while uy1 <= end[0]:
            ocean_floor[start[1]][uy1]+=1
            if ocean_floor[start[1]][uy1] == 2:
                overlapping_point+=1
            uy1+=1
    # Vertical lines
    if start[0] == end[0]:
        while ux1 <= end[1]:
            ocean_floor[ux1][start[0]]+=1
            if ocean_floor[ux1][start[0]] == 2:
                overlapping_point+=1
            ux1+=1

print(overlapping_point)