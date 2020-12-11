from pprint import pprint

file_input = open("input.txt", "r")
txt = file_input.read().splitlines()

# data structure : [[0,1,2],[0,1,2], ... ]
# 
# [
# 0,0  [],
# 1,0  [],
# ] 

tree_map = []

for line in txt:
    topology = []
    for data_pt in line:
        if data_pt == '#':
            topology.append(True)
            continue
        topology.append(False)
    tree_map.append(topology)

size = len(tree_map)
length = len(tree_map[0])

x_intervals = [1, 3, 5, 7, 1]
y_intervals = [1, 1, 1, 1, 2]
num_trees_total = 1

for interval_idx in range(len(x_intervals)):
    x_interval = x_intervals[interval_idx]
    y_interval = y_intervals[interval_idx]
    cur_x = 0
    cur_y = 0
    num_trees = 0
    while cur_y < size - 1:
        cur_x = (cur_x + x_interval) % length
        cur_y += y_interval
        try:
            if tree_map[cur_y][cur_x]:
                num_trees += 1
        except IndexError:
            continue
    num_trees_total *= num_trees


print(num_trees_total)
