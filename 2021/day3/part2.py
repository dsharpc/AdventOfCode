
import operator

with open('input.txt', 'r') as f:
    input = f.read().splitlines()

row_len = len(input[0])

oxynums = input.copy()
co2nums = input.copy()


def get_number(array, most_common=True):
    if most_common:
        op = operator.le
    else:
        op = operator.gt

    for i in range(row_len):
        one_bits = 0
        if len(array) == 1:
            break
        for line in array:
            if list(line)[i] == '1':
                one_bits+=1
        if op(len(array) - one_bits, one_bits):
            filter_ = '1'
        else:
            filter_ = '0'
        array = [x for x in array if x[i] == filter_]
    
    return int(array[0],2)

oxy = get_number(oxynums)
co2 = get_number(co2nums, False)
print(oxy*co2)
