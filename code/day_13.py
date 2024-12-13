import numpy as np
import re


def parse_input(input_data: str):

    m = []
    arr = []
    count = 1
    with open(input_data, "r") as file:

        for line in file:
            if count % 4 != 0:
                values = re.findall(r"\d+", line)
                arr += [values]
            else:
                m += [arr]
                arr = []
            count += 1
    m += [arr]

    return np.array(m).astype(int)


def get_new_coordinates(v1, v2, v):
    M = np.column_stack((v1, v2))
    M_inv = np.linalg.inv(M)
    return M_inv.dot(v)


def check_solution(coords, v1, v2, v, thresh):
    if round(coords[0]) >= thresh or round(coords[1]) >= thresh:
        return False
    check_a = round(coords[0]) * round(v1[0]) + round(coords[1]) * round(v2[0])
    check_b = round(coords[0]) * round(v1[1]) + round(coords[1]) * round(v2[1])
    check = check_a == round(v[0]) and check_b == round(v[1])

    return check


def p1(m) -> int:
    cost = 0

    for mi in m:

        v = np.array(mi[2])
        v1 = np.array(mi[0])
        v2 = np.array(mi[1])

        coords = get_new_coordinates(v1, v2, v)

        cost_mi = 3 * round(coords[0]) + round(coords[1])

        if check_solution(coords, v1, v2, v, 100):
            cost += cost_mi

    return cost


def p2(m) -> int:
    cost = 0
    for mi in m:

        v = np.array(mi[2]) + 10000000000000
        v1 = np.array(mi[0])
        v2 = np.array(mi[1])

        coords = get_new_coordinates(v1, v2, v)

        cost_mi = 3 * round(coords[0]) + round(coords[1])

        if check_solution(coords, v1, v2, v, 1e30):
            cost += cost_mi

    return cost


def main(input_data):

    m = parse_input(input_data)

    return p1(m), p2(m)
