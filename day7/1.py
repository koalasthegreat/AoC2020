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

def count_shiny(bag_map):
    def _helper(bag_name):
        if bag_name == "shiny gold":
            return True

        if bag_map.get(bag_name) is not None:
            if bag_map[bag_name]:
                for bag in bag_map[bag_name]:
                    if _helper(bag[0]):
                        return True
        return False

    count = 0

    for key in bag_map.keys():
        if key != "shiny gold":
            if _helper(key):
                count += 1
        
    return count


lines = sys.stdin.readlines()
bag_map = parse_lines(lines)
count = count_shiny(bag_map)

print(count)
