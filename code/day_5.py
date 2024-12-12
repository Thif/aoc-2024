import numpy as np
from typing import Tuple, List
import random


def parse_input(input_data: str) -> Tuple[List[int], List[int]]:

    v1 = []
    v2 = []

    with open(input_data, "r") as file:
        for line in file:
            if "|" in line:
                v1 += [[int(a) for a in line[:-1].split("|")]]
            if "," in line:
                if "\n" in line:
                    v2 += [[int(a) for a in line[:-1].split(",")]]
                else:
                    v2 += [[int(a) for a in line.split(",")]]

    return v1, v2


def check_valid(s, v):
    checks = []
    for c in v:
        if c[0] in s and c[1] in s:
            checks += [s.index(c[0]) < s.index(c[1])]
    return np.array(checks).all()


def fix_list(s, v):
    random.shuffle(v)
    for c in v:
        if c[0] in s and c[1] in s:
            index_0 = s.index(c[0])
            index_1 = s.index(c[1])
            if not index_0 < index_1:
                s[index_0], s[index_1] = s[index_1], s[index_0]

    return check_valid(s, v), s


def p1(v1, v2) -> int:
    middle_sum = 0
    for l in v2:
        is_valid = check_valid(l, v1)
        if is_valid:
            middle_sum += l[int(len(l) / 2)]

    return middle_sum


def p2(v1, v2) -> int:
    middle_sum = 0
    for l in v2:
        is_valid = check_valid(l, v1)
        if not is_valid:
            is_corrected = False
            while not is_corrected:
                is_corrected, l = fix_list(l, v1)
            middle_sum += l[int(len(l) / 2)]

    return middle_sum


def main(input_data):
    v1, v2 = parse_input(input_data)
    return p1(v1, v2), p2(v1, v2)
