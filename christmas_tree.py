def christmasTree(levelNum, levelHeight):
    result = []
    result += crown()

    w = 5
    for l in range(levelNum):
        result += level(w, levelHeight)
        w += 2

    result += foot(levelNum, levelHeight)

    # get the largest offset
    m = min([r[0] for r in result])

    f = lambda row: ''.join(['*' if i in row else ' ' for i in range(m, row[-1]+1)])
    result = [f(r) for r in result]
    return result


def crown():
    return [[0], [0], [-1, 0, 1]]


def foot(h, w):
    result = []
    w = w if w % 2 == 1 else w + 1
    for i in range(h):
        result.append(row(w))
    return result


def level(w, h):
    result = []
    for i in range(h):
        result.append(row(w))
        w += 2
    return result


def row(w):
    return [j - (w - 1) / 2 for j in range(w)]


print christmasTree(1, 3)
