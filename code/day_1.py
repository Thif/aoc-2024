import numpy as np
import sys
from typing import Tuple, List


def parse_input(input_data: str) -> Tuple[List[int], List[int]]:

    v1 = []
    v2 = []

    with open(input_data, "r") as file:
        for line in file:

            c1, c2 = line.split()  # Split by whitespace

            v1.append(int(c1))
            v2.append(int(c2))

    return v1, v2


def p1(v1: List[int], v2: List[int]) -> int:

    sorted_v1 = sorted(v1)
    sorted_v2 = sorted(v2)

    return sum(abs(a - b) for a, b in zip(sorted_v1, sorted_v2))


def p2(v1: List[int], v2: List[int]) -> int:

    similarity = []

    for v in v1:
        count = v2.count(v)
        if count > 0:
            similarity.append(v * count)

    return sum(similarity)


"""
Optimized version using Counter from collections
def p2(v1: List[int], v2: List[int]) -> int:
    counter1 = Counter(v1)
    counter2 = Counter(v2)
    # Compute the sum of intersections with counts in O(n)
    return sum(min(counter1[v], counter2[v]) * v for v in counter1)
"""


def main(input_data):
    v1, v2 = parse_input(input_data)
    print(p1(v1, v2), p2(v1, v2))
