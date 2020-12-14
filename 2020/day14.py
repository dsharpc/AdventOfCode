import re
INPUT_FILE = 'inputs/day14_input.txt'


def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    return data

def parse_mask(mask_str):
    mask = []
    mask_str = mask_str.replace('mask = ','').strip()
    for i, el in enumerate(mask_str[::-1]):
        mask.append((i, el))
    return mask

def parse_data(data_row):
    address, value = data_row.strip().split(' = ')
    address = re.search(r'.*\[(\d+)\]', address).group(1)
    return address, int(value)

def mask_value(mask, value):
    res = value
    for idx, bit in mask:
        if bit == '1':
            res = res | 1 << idx
        elif bit == '0':
            res = res & ~(1 << idx)
    return res

def main_part1():
    data = load_data()
    memory = {}
    for row in data:
        if 'mask' in row:
            mask = parse_mask(row)
        elif 'mem' in row:
            address, value = parse_data(row)
            memory[address] = mask_value(mask, value)
    print(sum(memory.values()))

# main_part1()

def generate_masks(mask, i=0, running_mask='',masks = []):
    mask = mask.copy()
    if i == len(mask):
        masks.append(running_mask)
    elif mask[i] == 'X':
        mask_1 = mask
        mask_1[i] = '1'
        generate_masks(mask_1, i, running_mask, masks)
        mask_0 = mask
        mask_0[i] = '0'
        generate_masks(mask_0, i, running_mask, masks)
    else:
        running_mask+=mask[i]
        i+=1
        generate_masks(mask, i, running_mask, masks)

    return masks


def mask_address(mask, address):
    mask = mask.copy()
    res = [c for c in f"{int(address):036b}"][::-1]
    for idx, bit in enumerate(mask):
        if res[idx] == '1':
            if mask[idx] != 'X':
                mask[idx] = '1'
    return mask

def main_part2():
    data = load_data()
    memory = {}
    for row in data:
        if 'mask' in row:
            mask = parse_mask(row)
            mask = [bit for _, bit in mask]
        elif 'mem' in row:
            address, value = parse_data(row)
            add = mask_address(mask, address)
            masks = generate_masks(add, masks = [])
            for m in masks:
                ad = int(m[::-1],2)
                memory[ad] = value
    print(sum(memory.values()))
main_part2()