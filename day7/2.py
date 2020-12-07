import sys

def parse_lines(lines):
    bag_map = {}

    for line in lines:
        if line != "\n":
            words = [x.strip("\n").strip(".").strip(",") for x in line.split(" ")]

            outer_bag = words[0] + " " + words[1]

            if (words[4] == "no"):
                bag_map[outer_bag] = False
            else:
                for i in range(4, len(words), 4):
                    num = int(words[i])
                    inner_bag = words[i + 1] + " " + words[i + 2]

                    if bag_map.get(outer_bag) is None:
                        bag_map[outer_bag] = []

                    bag_map[outer_bag].append([inner_bag, num])
    return bag_map

def sum_bags(bag_map, bag_name):
    def _helper(bag_name):
        if bag_map.get(bag_name) is not None:
            if bag_map[bag_name]:
                total = 1

                for bag in bag_map[bag_name]:
                    total += bag[1]*_helper(bag[0])

                return total
        return 1

    return _helper(bag_name) - 1


lines = sys.stdin.readlines()
bag_map = parse_lines(lines)
total = sum_bags(bag_map, "shiny gold")

print(total)
