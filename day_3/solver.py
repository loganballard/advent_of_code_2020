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

cur_x = 0
cur_y = 0
num_trees = 0
size = len(tree_map)
length = len(tree_map[0])

while cur_y < size - 1:
    cur_x = (cur_x + 3) % length
    cur_y += 1
    if tree_map[cur_y][cur_x]:
        print(cur_x)
        print(txt[cur_y])
        num_trees += 1
print(num_trees)
