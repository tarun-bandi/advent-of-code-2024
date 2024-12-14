"""
We want to write a program that parses mul(x, y) in strings.
"""

import re
def get_input():

    res = None

    with open("input1.txt", "r") as file:
        res = file.read()

    return res


def find_muls(input_string):
    target = r"mul\(\d+,\d+\)"
    target2 = r"don't\(\)"
    target3 = r"do\(\)"
    targets = [target, target2, target3]
    instances = re.findall("|".join(targets), input_string)

    total = 0
    use = True
    for instance in instances:
        if instance == "do()":
            use = True
        elif instance == "don't()":
            use = False
        else:
            instance = instance[4:] #remove mul(

            first, second = instance.split(",")
            second = second[:-1]

            if use:
                total += int(second) * int(first)

    return total

input = get_input  ()
print(find_muls(input))

