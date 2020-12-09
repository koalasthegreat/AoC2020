import sys

def process_input(lines):
    out = []

    for line in lines:
        out.append(int(line.strip("\n")))

    return out

def check_valid(n, l):
    for index, x in enumerate(l):
        for i in range(len(l)):
            if i != index:
                if x + l[i] == n:
                    return True
    return False

def find_outlier(numbers, preamble):
    working_list = []

    for i in range(preamble):
        working_list.append(numbers.pop(0))

    while len(numbers) > 0:
        number = numbers.pop(0)

        if not check_valid(number, working_list):
            return number

        working_list.pop(0)
        working_list.append(number)


lines = sys.stdin.readlines()
numbers = process_input(lines)
print(find_outlier(list(numbers), 25))
