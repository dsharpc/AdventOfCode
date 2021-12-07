with open('input.txt', 'r') as f:
    input = f.read().split(',')

lanternfish = [int(x) for x in input]

NUM_DAYS = 80

day=0
while day < NUM_DAYS:
    for i, fish in enumerate(lanternfish):
        if fish == 0:
            lanternfish.append(9)
            lanternfish[i] = 6
        else:
            lanternfish[i]-=1
    day+=1

print(len(lanternfish))
            