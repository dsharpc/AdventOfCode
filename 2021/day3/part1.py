
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

gamma_rate = []
epsilon_rate = []

row_len = len(input[0])

for i in range(row_len):
    one_bits = 0
    for line in input:
        if list(line)[i] == '1':
           one_bits+=1

    if one_bits > len(input)//2:
        gamma_rate.append('1')
        epsilon_rate.append('0')
    else:
        gamma_rate.append('0')
        epsilon_rate.append('1')

gamma = ''.join(gamma_rate)
epsilon = ''.join(epsilon_rate)

print(int(gamma,2) * int(epsilon, 2))
