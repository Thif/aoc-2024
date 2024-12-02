import numpy as np
import sys
from typing import Tuple, List


def parse_input(input_data_path: str) -> List:

    with open(input_data_path,"r") as f:
        m=[np.array(x.split()).astype(int) for x in f.readlines()]

    return m


def check_value(v)->int:
    return int((np.isin(np.diff(v),[1,2,3])).all()  | (np.isin(np.diff(v),[-1,-2,-3])).all())

def p1(l:List) -> int:

    tot=0
    for v in l:
        tot+=check_value(v)

    return tot


def p2(l:List) -> int:

    tot=0
    for v in l:
        check=check_value(v)

        if check:
            tot+=check
            print(v,check)
        else:
            check_popped=[check_value(np.delete(v,i)) for i in range(len(v))]
            tot+=max(check_popped)

    return tot


def main(input_data):
    m = parse_input(input_data)
    print(p1(m), p2(m))
