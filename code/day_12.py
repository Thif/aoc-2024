import numpy as np


def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                l_list = [c for c in line[:-1]]
            else:
                l_list = [c for c in line]

            m.append(l_list)

    return np.array(m)


def get_connections(m):

    connections = {}
    fences = {}
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            letter = m[i, j]
            connections[(i, j)] = []
            fences[(i, j)] = [0]  # dummy orientation ( center )

            if i > 0:
                a = m[i - 1, j]
                if a == letter:
                    connections[(i, j)] += [(i - 1, j)]
                else:
                    fences[(i, j)] += [1]
            if i < m.shape[0] - 1:
                a = m[i + 1, j]
                if a == letter:
                    connections[(i, j)] += [(i + 1, j)]
                else:
                    fences[(i, j)] += [3]
            if j > 0:
                a = m[i, j - 1]
                if a == letter:
                    connections[(i, j)] += [(i, j - 1)]
                else:
                    fences[(i, j)] += [4]
            if j < m.shape[1] - 1:
                a = m[i, j + 1]
                if a == letter:
                    connections[(i, j)] += [(i, j + 1)]
                else:
                    fences[(i, j)] += [2]

            # fences for non neighboring
            if i == 0:
                fences[(i, j)] += [1]
            if j == 0:
                fences[(i, j)] += [4]
            if i == m.shape[0] - 1:
                fences[(i, j)] += [3]
            if j == m.shape[1] - 1:
                fences[(i, j)] += [2]

    return connections, fences


def get_linked(ind, cluster, connections, fence_orient, fences):
    # no connected letters
    if len(connections[ind]) == 0:
        return [ind]

    if ind not in cluster and fence_orient in fences[ind]:
        cluster += [ind]

    if all(n in cluster for n in connections[ind]):
        return cluster

    for n in connections[ind]:
        if n not in cluster and fence_orient in fences[n]:
            cluster = get_linked(n, cluster, connections, fence_orient, fences)

    return cluster


def get_clusters_fences(c, fence_orient, fences, connections):
    clusters = []
    for ind in c:
        if fence_orient not in fences[ind]:
            continue

        if sum([int(ind in c) for c in clusters]) > 0:
            continue

        clusters += [get_linked(ind, [], connections, fence_orient, fences)]

    return clusters


def p1(m) -> int:

    connections, fences = get_connections(m)

    clusters = get_clusters_fences(connections.keys(), 0, fences, connections)

    total = 0

    for c in clusters:

        area = len(c)
        perimeter = sum([4 - len(connections[v]) for v in c])
        total += area * perimeter

    return total


def p2(m) -> int:

    connections, fences = get_connections(m)

    clusters = []
    total = 0
    clusters = get_clusters_fences(connections.keys(), 0, fences, connections)

    for i, c in enumerate(clusters):
        clusters_up = get_clusters_fences(c, 1, fences, connections)
        clusters_down = get_clusters_fences(c, 3, fences, connections)
        clusters_right = get_clusters_fences(c, 2, fences, connections)
        clusters_left = get_clusters_fences(c, 4, fences, connections)

        area = len(c)
        perimeter = (
            len(clusters_up)
            + len(clusters_down)
            + len(clusters_left)
            + len(clusters_right)
        )

        total += area * perimeter

    return total


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
