from itertools import product


def parse_input(input_data: str):

    v = []

    with open(input_data, "r") as file:
        for line in file:

            if "\n" in line:
                line = line[:-1]

            a = line.split()
            a[0] = a[0].split(":")[0]
            v += [[int(x) for x in a]]

    return v


def check_possible_combinations(v):

    goal = v[0]
    elements = v[1:]
    ops = product("*+", repeat=len(elements) - 1)

    for lo in ops:
        tmp = elements[0]
        for o, e in zip(lo, elements[1:]):

            if o == "+":
                tmp += e
            elif o == "*":
                tmp *= e
        if tmp == goal:
            return True, lo

    return False, None


def p1(m) -> int:
    total = 0
    for v in m:
        val, ops = check_possible_combinations(v)
        if val:
            total += v[0]

    return total


def check_more_possible_combinations(v):

    goal = v[0]
    elements = v[1:]
    ops = product("*+C", repeat=len(elements) - 1)

    for lo in ops:

        tmp = elements[0]
        for i, (o, e) in enumerate(zip(lo, elements[1:])):

            if o == "+":
                tmp += e
            elif o == "*":
                tmp *= e
            elif o == "C":
                tmp = int(str(tmp) + str(e))

        if tmp == goal:
            return True, lo

    return False, None


def p2(m) -> int:
    total = 0
    for v in m:

        val, lo = check_more_possible_combinations(v)

        if val:
            total += v[0]

    return total


def main(input_data):

    m = parse_input(input_data)

    return (p1(m.copy()), p2(m.copy()))
