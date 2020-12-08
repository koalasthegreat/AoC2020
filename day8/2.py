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
                return False
        
        ran.append([instruction, cur])

        if instruction[0] == "jmp":
            cur += instruction[1]
        else:
            cur += 1

        if instruction[0] == "acc":
            acc += instruction[1]
    return acc

def modify_instructions(instructions):
    for index, instruction in enumerate(instructions):
        if instruction[0] == "jmp":
            new_instructions = list(instructions)
            new_instructions[index] = ["nop", instruction[1]]
            
            result = run_machine(new_instructions)

            if result:
                return result

        elif instruction[0] == "nop":
            new_instructions = list(instructions)
            new_instructions[index] = ["jmp", instruction[1]]
            
            result = run_machine(new_instructions)

            if result:
                return result


instructions = parse_input(sys.stdin.readlines())
print(modify_instructions(instructions))
