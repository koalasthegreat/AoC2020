import sys

def process_input(lines):
    tree_map = []

    for line in lines:
        row = []

        for char in line.strip("\n"):
            row.append(char)

        tree_map.append(row)

    return tree_map

def check_slope(x, y, tree_map):
    pos = [0, 0]
    count = 0

    while pos[1] < len(tree_map):
        if tree_map[pos[1]][pos[0]] == "#":
            count += 1

        pos[0] = (pos[0] + x) % len(tree_map[0])
        pos[1] += y

    return count

lines = sys.stdin.readlines()
tree_map = process_input(lines)

pairs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total = 1

for pair in pairs:
    total = total * check_slope(pair[0], pair[1], tree_map)

print(total)