import sys
import re

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
        if len(field.split(":")) < 2:
            continue

        key, value = field.split(":")

        if key == "byr":
            try:
                value = int(value)
                if 1920 <= value <= 2002:
                    fields[key] = True
            except:
                pass

        elif key == "iyr":
            try:
                value = int(value)
                if 2010 <= value <= 2020:
                    fields[key] = True
            except:
                pass

        elif key == "eyr":
            try:
                value = int(value)
                if 2020 <= value <= 2030:
                    fields[key] = True
            except:
                pass

        elif key == "hgt":
            unit = value[-2:]
            value = value[:-2]
            try:
                value = int(value)
                if unit == "cm" and 150 <= value <= 193:
                    fields[key] = True
                elif unit == "in" and 59 <= value <= 76:
                    fields[key] = True
            except:
                pass

        elif key == "hcl":
            if re.match("^#[a-f0-9]{6}$", value):
                fields[key] = True

        elif key == "ecl":
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                fields[key] = True

        elif key == "pid":
            if re.match("^[0-9]{9}$", value):
                fields[key] = True

        elif key == "cid":
            fields[key] = True

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
