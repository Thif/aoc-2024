import numpy as np


def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                l = [int(c) for c in line[:-1]]
            else:
                l = [int(c) for c in line]

            m.append(l)

    return np.array(m)


def p1(m) -> int:

    return


def p2(m) -> int:

    return


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy())
