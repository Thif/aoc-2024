import numpy as np
import re


def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                print("new line")
                l = line[:-1]  # Split by whitespace
            else:
                l = line

            m.append(l)

    return np.array(m)[0]


def move_to_left_most(s):
    first_match = s.index(".")

    for i, u in enumerate(s[::-1]):

        if u != ".":
            end_index = len(s) - i - 1
            break

    s[first_match] = s[end_index]
    s[end_index] = "."
    return s


def generate_list(m):
    out_list = []
    count = 0
    ids = {}
    for i, c in enumerate(m):
        if i % 2 == 0:
            ids[count] = int(c)
            for i in range(int(c)):
                out_list += [str(count)]

            count += 1
        else:
            out_list += ["."] * int(c)
    return out_list, ids


def get_checksum(files):
    return sum(i * int(file) for i, file in enumerate(files) if file.isdigit())


def p1(m) -> int:

    out_list, ids = generate_list(m)
    # print(out_list)

    new_list = out_list.copy()

    n_groups = 1e6
    while n_groups > 1:

        print(n_groups)
        new_list = move_to_left_most(new_list)
        matches = re.findall("\.+", "".join(new_list))
        n_groups = len([m for m in matches])

    checksum = get_checksum(new_list)
    return checksum


def get_empty_spots_list(disk_layout_list):
    empty_spots = []
    start_index = None

    for i, block in enumerate(disk_layout_list):
        if block == ".":
            if start_index is None:
                start_index = i
        else:
            if start_index is not None:
                empty_spots.append((start_index, i))
                start_index = None

    if start_index is not None:
        empty_spots.append((start_index, len(disk_layout_list)))

    return empty_spots


def p2(m) -> int:

    out_list, ids = generate_list(m)

    # print(len(out_list))
    # print(ids)
    new_list = out_list.copy()
    for id, size in reversed(list(ids.items())):
        # print("".join(new_list))
        # print(id)
        # if id<9998:break
        # print(id,size)
        current_index = new_list.index(str(id))

        # print(new_list[:current_index])
        empty_spots = get_empty_spots_list(new_list[:current_index])
        # print(empty_spots)
        if len(empty_spots) == 0:
            break
        # print("".join(new_list))
        # print("".join(new_list[-35:]))
        # print(new_list[-5:])
        # print(empty_spots[:10])
        for i, l in enumerate(empty_spots):

            if size <= l[1] - l[0]:
                # print(id,"to",i,l)
                new_list = ["." if s == str(id) else s for s in new_list]

                for j in range(size):
                    new_list[l[0] + j] = str(id)

                break

    print(new_list.count(".") == out_list.count("."))

    checksum = get_checksum(new_list)
    # print("".join(new_list))
    # print(len(new_list))
    return checksum


def main(input_data):

    m = parse_input(input_data)

    return p2(m.copy())
