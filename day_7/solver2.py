import os, pprint
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()

class Bag:
    adjective = None
    color = None
    contents: list = None  # list bag, count
    contains_bag_num: int = 0

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
                new_bag.contents.append((sub_bag_tup, sub_bag_number))
                new_bag.contains_bag_num += int(sub_bag_number)
        bag_obj_map[(adjective, color)] = new_bag


def count_sub_bags(bag: Bag) -> int:
    if not bag.contents:
        return bag.contains_bag_num
    sub_cnt = 0
    for sub_bag in bag.contents:
        num_of_sub_bags = int(sub_bag[1])
        sub_cnt += (num_of_sub_bags * count_sub_bags(bag_obj_map[sub_bag[0]]))
    return sub_cnt + bag.contains_bag_num


print(count_sub_bags(bag_obj_map[('shiny', 'gold')]))