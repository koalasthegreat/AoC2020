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

    while True:
        number = numbers.pop(0)

        if not check_valid(number, working_list):
            return number

        working_list.pop(0)
        working_list.append(number)

def find_contiguous_list(numbers, invalid):
    while len(numbers) > 0:
        contiguous_list = []
        total = numbers.pop(0)
        contiguous_list.append(total)
        
        for number in numbers:
            total += number
            contiguous_list.append(number)
            
            if total == invalid:
                return contiguous_list
            if total > invalid:
                break


lines = sys.stdin.readlines()
numbers = process_input(lines)
invalid_number = find_outlier(list(numbers), 25)
contiguous_list = find_contiguous_list(numbers, invalid_number)
print(min(contiguous_list) + max(contiguous_list))
