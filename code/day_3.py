from typing import List
import re
import math


def parse_input(input_data_path: str) -> str:

    with open(input_data_path, "r") as f:
        m = f.read()
    return m


def p1(l: str) -> int:

    matches = re.findall("mul\(\d+,\d+\)", l)

    products = sum(
        [
            math.prod([int(x) for x in vi.split("mul")[-1][1:-1].split(",")])
            for vi in matches
        ]
    )

    return products


def p2(input_list: List) -> int:
    products = 0
    parts = re.split(
        "(do\(\)|don't\(\))", input_list
    )  # keeps do() or don't() in matches so that we can check preceding condition

    for i, chunck in enumerate(parts):
        if i == 0 or parts[i - 1] == "do()":
            matches = re.findall("mul\(\d+,\d+\)", chunck)
            products += sum(
                [
                    math.prod([int(x) for x in vi.split("mul")[-1][1:-1].split(",")])
                    for vi in matches
                ]
            )

    return products


def main(input_data):
    m = parse_input(input_data)
    return (p1(m), p2(m))
