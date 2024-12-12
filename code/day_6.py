import numpy as np


def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                l = [a for a in line[:-1]]  # Split by whitespace
            else:
                l = [a for a in line]

            m.append(l)

    return np.array(m)


def get_guard_position(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i, j] == "^":
                return (i, j)


def get_visited_positions(m, coord):
    col = m[: coord[0], coord[1]]

    match_block_array = np.where(col == "#")

    if match_block_array[0].size != 0:  # there are blocks
        last_coord = match_block_array[0][-1]  # next block coordinates

        if last_coord + 1 != coord[0]:
            m[last_coord + 1 : coord[0] + 1, coord[1]] = "X"
            m[last_coord + 1, coord[1]] = "^"
    else:  # no block we go upmost
        last_coord = 0
        m[last_coord : coord[0] + 1, coord[1]] = "X"

    return m


def update_with_positions(m):
    coord = get_guard_position(m)
    m = get_visited_positions(m, coord)
    return m


def points_between(points):

    x1, y1 = points[0]
    x2, y2 = points[1]

    if x1 == x2:
        if y1 < y2:
            points_between = [(x1, y) for y in range(y1, y2)]
        else:
            points_between = [(x1, y) for y in range(y1, y2, -1)]
    if y1 == y2:
        if x1 < x2:
            points_between = [(x, y1) for x in range(x1, x2)]
        else:
            points_between = [(x, y1) for x in range(x1, x2, -1)]
    return points_between


def get_intermediate_positions(guard_positions, init_pos, new_pos, shape):

    if new_pos is None:
        # check where it was coming from
        diff0 = init_pos[0] - guard_positions[-1][0]
        diff1 = init_pos[1] - guard_positions[-1][1]

        if diff0 == 0 and diff1 > 0:  # down
            new_pos = (shape[0] - 1, init_pos[1])
        elif diff0 == 0 and diff1 < 0:  # up
            new_pos = (0, init_pos[1])
        elif diff0 < 0 and diff1 == 0:  # right
            new_pos = (init_pos[0], shape[1] - 1)
        else:
            new_pos = (init_pos[0], 0)

        intermediate_points = points_between([init_pos, new_pos]) + [new_pos]
    else:
        intermediate_points = points_between([init_pos, new_pos])
    for p in intermediate_points:
        guard_positions += [p]
    return guard_positions


def p1(m, record_positions=True) -> int:

    converged = False
    rot_count = 0
    guard_positions = []
    all_guard_positions = []

    for i in range(1000000):

        # check for loop
        init_guard_pos = get_guard_position(np.rot90(m, k=4 - rot_count % 4))

        is_loop = sum(np.array_equal(init_guard_pos, p) for p in guard_positions) > 4

        if is_loop:
            break

        m = update_with_positions(m)

        new_guard_pos = get_guard_position(np.rot90(m, k=4 - rot_count % 4))

        if record_positions:
            all_guard_positions = get_intermediate_positions(
                all_guard_positions, init_guard_pos, new_guard_pos, m.shape
            )

        # leave if guard is off
        if "^" not in m:
            converged = True
            break
        guard_positions += [init_guard_pos]

        # rotate matrix
        m = np.rot90(m)
        rot_count += 1

    return (
        converged,
        len(np.where(m == "X")[0]),
        np.rot90(m, 4 - rot_count % 4),
        all_guard_positions,
    )


def p2(m) -> int:
    count = 0

    converged, _, final_m, positions = p1(m.copy())

    unique_pos = list(set(positions))

    for i, pos in enumerate(unique_pos):
        init_m = m.copy()

        if init_m[pos] == "^":
            continue

        init_m[pos] = "#"

        c = p1(init_m, False)

        if not c[0]:
            count += 1

    return count


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
