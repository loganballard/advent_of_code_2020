import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

file_input = open("".join([dir_path, "/", "input.txt"]), "r")
txt = file_input.read().splitlines()

class Bag:
    adjective = None
    color = None
    contains = []  # list of bags


bag_obj_map = {}  # (adj, clr) --> Bag


# build obj map
for line in txt:
    words = line.split()
    adjective, color = words[0], words[1]
    if not bag_obj_map.get((adjective, color), None):
        new_bag = Bag()
        new_bag.adjective = adjective
        new_bag.color = color
        bag_obj_map[(adjective, color)] = new_bag

print(bag_obj_map)
