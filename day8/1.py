import sys

def parse_input(lines):
    instructions = []

    for line in lines:
        line = line.strip("\n").split(" ")

        instruction = line[0]
        number = int(line[1])

        instructions.append([instruction, number])

    return instructions
        
def run_machine(instructions):
    acc = 0
    cur = 0
    ran = []

    while cur < len(instructions):
        instruction = instructions[cur]

        for ins in ran:
            if ins[0] == instruction and ins[1] == cur:
                return acc
        
        ran.append([instruction, cur])

        if instruction[0] == "jmp":
            cur += instruction[1]
        else:
            cur += 1

        if instruction[0] == "acc":
            acc += instruction[1]


instructions = parse_input(sys.stdin.readlines())
print(run_machine(instructions))
