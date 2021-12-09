from collections import Counter

with open('input.txt', 'r') as f:
    input = f.readlines()


data = [(x.split('|')[0].split(), x.split('|')[1].split()) for x in input]

def code_back_to_number(output, codified):
    letters = list(output)
    lights = []
    for letter in letters:
        lights.append(list(codified.keys())[list(codified.values()).index(letter)])
    if len(letters) == 2:
        return '1'
    elif len(letters) == 3:
        return '7'
    elif len(letters) == 4:
        return '4'
    elif len(letters) == 7:
        return '8'
    elif set(lights) == set(['vbr', 'vbl','vtl','hb', 'vtr','ht']):
        return '0'
    elif set(lights) == set(['ht','vtr','hm','vbl','hb']):
        return '2'
    elif set(lights) == set(['ht','vtr','hm','vbr','hb']):
        return '3'
    elif set(lights) == set(['ht','vtl','hm','vbr','hb']):
        return '5'
    elif set(lights) == set(['ht','vtl','hm','vbl','vbr','hb']):
        return '6'
    elif set(lights) == set(['ht', 'vtl', 'vtr', 'hm', 'vbr', 'hb']):
        return '9'


acum = 0

# Code signals back to numbers
for signal, output in data:
    alloc = {}
    sig = ''.join(signal)
    counted = Counter(sig)
    alloc['vbr'] = list(counted.keys())[list(counted.values()).index(9)]
    del counted[alloc['vbr']]
    alloc['vbl'] = list(counted.keys())[list(counted.values()).index(4)]
    del counted[alloc['vbl']]
    alloc['vtl'] = list(counted.keys())[list(counted.values()).index(6)]
    del counted[alloc['vtl']]

    for sign in sorted(signal, key=len):
        if len(sign) == 2:
            lsign = list(sign)
            for l in lsign:
                if l not in alloc.values():
                    alloc['vtr'] = l
                    del counted[alloc['vtr']]
            alloc['ht'] = list(counted.keys())[list(counted.values()).index(8)]
            del counted[alloc['ht']]
        if len(sign) == 4:
            lsign = list(sign)
            for l in lsign:
                if l not in alloc.values():
                    alloc['hm'] = l
                    del counted[alloc['hm']]
            alloc['hb'] = list(counted.keys())[list(counted.values()).index(7)]
            del counted[alloc['hb']]


    nums = []
    for out in output:
        nums.append(code_back_to_number(out, alloc))
        num = ''.join(nums)
        num = int(num)
    acum += num

print(acum)