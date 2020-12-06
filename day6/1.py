import sys

total = 0

for group in "".join(sys.stdin.readlines()).split("\n\n"):
    answers = set()

    for line in group:
        line = line.strip("\n")

        if line != "":
            for char in line:
                answers.add(char)

    total += len(answers)

print(total)
