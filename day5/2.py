import sys

def get_id(line):
    row_data = line[:7]
    column_data = line[7:]
    
    row = [0, 127]
    column = [0, 7]

    for index, char in enumerate(row_data):
        if index + 1 == len(row_data):
            if char == "F":
                row = int(row[0])
            elif char == "B":
                row = int(row[1])
            break

        if char == "F":
            row = [row[0], (row[0] + row[1])//2]
        elif char == "B":
            row = [(row[0] + row[1] + 1)//2, row[1]]

    for index, char in enumerate(column_data):
        if index + 1 == len(column_data):
            if char == "L":
                column = int(column[0])
            elif char == "R":
                column = int(column[1])
            break

        if char == "L":
            column = [column[0], (column[0] + column[1])//2]
        elif char == "R":
            column = [(column[0] + column[1] + 1)//2, column[1]]

    return(row * 8 + column)

lines = sys.stdin.readlines()
results = []

for line in lines:
    line = line.strip("\n")

    if len(line) != 0:
        results.append(get_id(line))

for i in range(40, 981):
    if i not in results:
        print(i)
