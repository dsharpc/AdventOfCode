import re

INPUT_FILE = 'inputs/day7_input.txt'
CONTENT_BAG_COLOUR = 'shiny gold'

def load_data():
    with open(INPUT_FILE,'r') as f:
        data = f.readlines()
    return data

def parse_data(data_line):
    reg = re.search(r'^(.*)bags contain (.*)',data_line)
    outer_bag = reg.group(1)
    inner_bags = reg.group(2)
    inner_bags = re.sub(r'\d','',inner_bags)
    inner_bags = re.sub(r'bag[s]?.','',inner_bags)
    inner_bags = inner_bags.split('  ')
    outer_bag = outer_bag.strip()
    inner_bags = [x.strip() for x in inner_bags]
    return outer_bag, inner_bags

def parse_data_part_2(data_line):
    reg = re.search(r'^(.*)bags contain (.*)',data_line)
    outer_bag = reg.group(1)
    inner_bags = reg.group(2)
    inner_bags = re.sub(r'bag[s]?.','',inner_bags)
    inner_bags = inner_bags.split('  ')
    outer_bag = outer_bag.strip()
    inner_bags = [tuple(x.strip().split(' ',1)) for x in inner_bags]
    return outer_bag, inner_bags

def search(rule_tree, bag_colour):
    matched = []
    for k,v in rule_tree.items():
        if bag_colour in v:
            matched.append(k)
            matched.extend(search(rule_tree, k))
    return matched

def search_part_2(rule_tree, bag_colour):
    bags = 1
    for k,v in rule_tree.items():
        if k == bag_colour:
            for item in v:
                if item[0] == 'no':
                    continue
                bags += int(item[0]) * search_part_2(rule_tree, item[1])
    return bags


def main_part_1():
    rule_tree = {}
    data = load_data()
    for e in data:
        outer_bag, inner_bags = parse_data(e)
        rule_tree[outer_bag] = inner_bags
    res = search(rule_tree, CONTENT_BAG_COLOUR)
    print(len(set(res)))
    

def main_part_2():
    rule_tree = {}
    data = load_data()
    for e in data:
        outer_bag, inner_bags = parse_data_part_2(e)
        rule_tree[outer_bag] = inner_bags
    res = search_part_2(rule_tree, CONTENT_BAG_COLOUR)
    print(res-1)
    


main_part_2()