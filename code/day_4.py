import numpy as np
from typing import Tuple, List
import re


def parse_input(input_data_path: str) -> str:

    m = np.loadtxt(input_data_path, dtype=str)
    m = [list(l) for l in m]
    return m


def p1(m: str) -> int:

    horizontal_mat = ["".join(l) for l in m]
    count_h = [
        len(re.findall("XMAS", n)) + len(re.findall("SAMX", n)) for n in horizontal_mat
    ]

    vertical_mat = ["".join(l) for l in np.rot90(m)]

    count_v = [
        len(re.findall("XMAS", n)) + len(re.findall("SAMX", n)) for n in vertical_mat
    ]

    diagonal_mat_1 = [
        "".join(np.diag(m, k=i))
        for i in range(-len(np.diag(m)) + 4, len(np.diag(m)) - 3)
    ]
    count_d1 = [
        len(re.findall("XMAS", n)) + len(re.findall("SAMX", n)) for n in diagonal_mat_1
    ]

    diagonal_mat_2 = [
        "".join(np.diag(np.rot90(m), k=i))
        for i in range(-len(np.diag(np.rot90(m))) + 4, len(np.diag(np.rot90(m))) - 3)
    ]
    count_d2 = [
        len(re.findall("XMAS", n)) + len(re.findall("SAMX", n)) for n in diagonal_mat_2
    ]

    return sum(count_v) + sum(count_h) + sum(count_d1) + sum(count_d2)


def p2(m: List) -> int:
    m = np.array(m)
    count = 0
    for i in range(0, m.shape[0] - 2):
        for j in range(0, m.shape[1] - 2):
            sub_mat = m[i : i + 3, j : j + 3]
            diag1 = np.diag(sub_mat)
            diag2 = np.diag(np.rot90(sub_mat))

            pattern = (
                (diag1 == ["M", "A", "S"]).all() | (diag1 == ["S", "A", "M"]).all()
            ) & ((diag2 == ["M", "A", "S"]).all() | ((diag2 == ["S", "A", "M"]).all()))

            if pattern:
                count += 1

    return count


def main(input_data):
    m = parse_input(input_data)

    return (p1(m), p2(m))
