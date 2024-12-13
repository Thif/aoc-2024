import numpy as np


def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                l_list = [int(c) for c in line[:-1]]
            else:
                l_list = [int(c) for c in line]

            m.append(l_list)

    return np.array(m)


def recursive_check(node, d_links, path=None, all_paths=None):
    if path is None:
        path = []
    if all_paths is None:
        all_paths = []

    path.append(node)

    if len(d_links[node]) == 0 and len(list(path)) == 10:
        all_paths.append(list(path))
    else:
        for t in d_links[node]:
            recursive_check(t, d_links, path, all_paths)

    path.pop()

    return all_paths


def p1(m) -> int:
    goal_indexes = [(int(a[0]), int(a[1])) for a in np.array(np.where(m == 9)).T]
    trailhead_indexes = [(int(a[0]), int(a[1])) for a in np.array(np.where(m == 0)).T]

    connections = {}
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            connections[(i, j)] = []
            if i > 0:
                a = m[i - 1, j] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i - 1, j)]
            if i < m.shape[0] - 1:
                a = m[i + 1, j] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i + 1, j)]
            if j > 0:
                a = m[i, j - 1] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i, j - 1)]
            if j < m.shape[1] - 1:
                a = m[i, j + 1] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i, j + 1)]

    scores = {}

    for th in trailhead_indexes:

        all_paths = recursive_check(th, connections)
        score = 0
        for g in goal_indexes:
            for p in all_paths:
                if g in p:
                    score += 1
                    break

        scores[th] = score

    sum_scores = sum([scores[k] for k in scores.keys()])

    return sum_scores


def p2(m) -> int:

    trailhead_indexes = [(int(a[0]), int(a[1])) for a in np.array(np.where(m == 0)).T]

    connections = {}
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            connections[(i, j)] = []
            if i > 0:
                a = m[i - 1, j] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i - 1, j)]
            if i < m.shape[0] - 1:
                a = m[i + 1, j] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i + 1, j)]
            if j > 0:
                a = m[i, j - 1] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i, j - 1)]
            if j < m.shape[1] - 1:
                a = m[i, j + 1] - m[i, j]
                if a == 1:
                    connections[(i, j)] += [(i, j + 1)]

    scores = {}

    for th in trailhead_indexes:

        all_paths = recursive_check(th, connections)
        scores[th] = len(all_paths)

    sum_scores = sum([scores[k] for k in scores.keys()])

    return sum_scores


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
