import numpy as np


def parse_input(input_data_path: str) -> np.array:

    m = np.loadtxt(input_data_path, dtype=str)
    m = [list(l) for l in m]
    return np.array(m)


def get_antinodes_matrix(m, m_an, c):

    points = np.array(np.where(m == c)).transpose()

    for point in points:
        for center in points:
            sym = get_symetric(point, center)
            if all(sym == point) or max(sym) > len(m) - 1 or min(sym) < 0:
                continue
            m_an[sym[0], sym[1]] = "#"

    return m_an


def get_symetric(point, center):
    sym = np.array([int(2 * center[0] - point[0]), int(2 * center[1] - point[1])])

    return sym


def p1(m) -> int:
    unique_chars = [s for s in np.unique(m) if s != "."]
    m_an = m.copy()
    for c in unique_chars:
        m_an = get_antinodes_matrix(m.copy(), m_an, c)

    return len(np.where(m_an == "#")[0])


def get_antinodes_matrix_resonance(m, m_an, c):

    points = np.array(np.where(m == c)).transpose()

    for point in points:
        for center in points:
            out = False
            point1 = point
            point2 = center
            while out == False:
                sym = get_symetric(point1, point2)

                if all(point2 == sym) or max(sym) > len(m) - 1 or min(sym) < 0:
                    out = True
                    continue
                point1 = point2
                point2 = sym
                m_an[sym[0], sym[1]] = "#"

    return m_an


def p2(m) -> int:
    unique_chars = [s for s in np.unique(m) if s != "."]
    m_an = m.copy()
    for c in unique_chars:
        m_an = get_antinodes_matrix_resonance(m.copy(), m_an, c)

    for c in unique_chars:
        m_an[m_an == c] = "#"

    return len(np.where(m_an == "#")[0])


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
