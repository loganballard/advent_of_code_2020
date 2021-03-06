import os, pprint
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()

class Bag:
    adjective = None
    color = None
    contents: list = None  # list of bags

    def __init__(self) -> None:
        super().__init__()
        self.contents = []



bag_obj_map = {}  # (adj, clr) --> Bag


# build obj map
for line in txt:
    words = line.split()
    adjective, color = words[0], words[1]
    contained_bags = words[4:]
    if not bag_obj_map.get((adjective, color), None):
        new_bag = Bag()
        new_bag.adjective = adjective
        new_bag.color = color
        if contained_bags[0] != 'no':
            while contained_bags:
                sub_bag_number = contained_bags.pop(0)
                sub_bag_adjective = contained_bags.pop(0)
                sub_bag_color = contained_bags.pop(0)
                contained_bags.pop(0)
                sub_bag_tup = (sub_bag_adjective, sub_bag_color)
                new_bag.contents.append(sub_bag_tup)
        bag_obj_map[(adjective, color)] = new_bag


bag_contains_gold_map = {
    ('shiny', 'gold'): True
}


def contains_gold_bag(bag: Bag) -> bool:
    bag_key = (bag.adjective, bag.color)
    if bag.adjective == 'shiny' and bag.color == 'gold':
        return True
    if bag_key in bag_contains_gold_map.keys():
        return True
    for sub_bag in bag.contents:
        if sub_bag in bag_contains_gold_map.keys() or contains_gold_bag(bag_obj_map[sub_bag]):
            bag_contains_gold_map[bag_key] = True
            return True
    return False

cnt = -1  # subtract one (gold bag can't hold itself)

for _, bag in bag_obj_map.items():
    if contains_gold_bag(bag):
        cnt += 1

print(cnt)
