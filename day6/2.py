import sys

total = 0

for group in "".join(sys.stdin.readlines()).split("\n\n"):
    answers = {}
    num_people = 0

    for line in group.split("\n"):
        line = line.strip("\n")

        if line != "":
            for char in line:
                if answers.get(char) is None:
                    answers[char] = 1
                else:
                    answers[char] = answers[char] + 1
            num_people += 1


    #print(answers, num_people)
    for value in answers.values():
        if value == num_people:
            total += 1
print(total)
