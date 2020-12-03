INPUT_FILE = 'inputs/day3_input.txt'

def load_data():
    with open(INPUT_FILE, 'r') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return data

def toboggan(forest, slope=(1,3)):
    row=0
    col=0
    trees=0
    while row < len(forest)-1:
        print(f"Row: {row}, col: {col}, trees: {trees}")
        row+=slope[0]
        col+=slope[1]
        if col >= len(forest[row]):
            col-=len(forest[row])
        if forest[row][col] == '#':
            trees+=1
    return trees
        
def main():
    data = load_data()
    trees = toboggan(data)
    print(trees)

def main_part2():
    data = load_data()
    slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    tree_mult = 1
    for slope in slopes:
        trees = toboggan(data, slope)
        tree_mult*=trees
    print(tree_mult)

if __name__=="__main__":
    main_part2()