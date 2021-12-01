
with open('input.txt', 'r') as f:
    input = f.readlines()

increases = 0
i = 1

while(i < len(input)):
    if(int(input[i-1]) < int(input[i])):
        increases+=1
    i+=1

print(increases)