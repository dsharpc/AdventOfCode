with open('input.txt', 'r') as f:
    input = f.readlines()


data = [(x.split('|')[0].split(), x.split('|')[1].split()) for x in input]

num_digits = 0

for signal, output in data:
    for value in output:
        if len(value) in [7, 4, 3, 2]:
            num_digits+=1

print(num_digits)