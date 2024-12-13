def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                l_list = [int(c) for c in line[:-1].split(" ")]
            else:
                l_list = [int(c) for c in line.split(" ")]

            m.append(l_list)

    return m[0]


# @cache can be used as well
precalc = {}


def num_stones(stone, blinks):
    if (stone, blinks) in precalc:
        return precalc[(stone, blinks)]

    if blinks == 0:
        return 1

    if stone == 0:
        return num_stones(1, blinks - 1)

    st = str(stone)
    if len(st) % 2 == 0:
        mid = len(st) // 2
        return num_stones(int(st[:mid]), blinks - 1) + num_stones(
            int(st[mid:]), blinks - 1
        )

    precalc[(stone, blinks)] = num_stones(stone * 2024, blinks - 1)
    return num_stones(stone * 2024, blinks - 1)


def p1(m):
    return sum([num_stones(st, 25) for st in m])


def p2(m):
    return sum([num_stones(st, 75) for st in m])


def main(input_data):

    m = parse_input(input_data)
    print(m)

    return p1(m.copy()), p2(m.copy())
