import sys

def process(raw_passport):
    processed = []

    for passport in raw_passport.split("\n\n"):
        p1 = passport.split("\n")
        p2 = []

        for elem in p1:
            if " " in elem:
                [p2.append(x) for x in elem.split(" ")]
            else:
                p2.append(elem)
        processed.append(p2)

    return processed

def validate(passport):
    fields = {
        "byr": False, 
        "iyr": False, 
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": False
        }

    for field in passport:
        if field[:3] in fields:
            fields[field[:3]] = True

    for key, value in fields.items():
        if not value:
            if key != "cid":
                return False

    return True


raw = "".join(sys.stdin.readlines())

passports = process(raw)

count = 0

for passport in passports:
    if validate(passport):
        count += 1

print(count)
