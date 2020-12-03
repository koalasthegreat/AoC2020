import sys

tree_map = []

for line in sys.stdin.readlines():
    row = []

    for char in line.strip("\n"):
        row.append(char)

    tree_map.append(row)

pos = [0, 0]
count = 0

while pos[1] < len(tree_map):
    if tree_map[pos[1]][pos[0]] == "#":
        count += 1

    pos[0] = (pos[0] + 3) % len(tree_map[0])
    pos[1] += 1

print(count)
