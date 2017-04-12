m = [[False, True, True],
          [True, True, False],
          [True, False, False]]


def span(max_, val):
    result = []
    if val > 0:
        result.append(val - 1)
    if val + 1 < max_:
        result.append(val + 1)
    return result


def neighbors(j, i, matrix):
    j_ = len(matrix)
    i_ = len(matrix[0])
    # print [(r, i, matrix[r][i]) for r in span(j_, j)] + [(j, c, matrix[j][c]) for c in span(i_, i)]
    return sum([1 for r in span(j_, j) if matrix[r][i]] + [1 for c in span(i_, i) if matrix[j][c]])


def polygonPerimeter(matrix):
    j_ = len(matrix)
    i_ = len(matrix[0])

    result = 0
    for j in range(j_):
        for i in range(i_):
            if matrix[j][i]:
                result += 4 - neighbors(j, i, matrix)

    return result


print polygonPerimeter(m)


