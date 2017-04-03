def reverseOnDiagonals(matrix):
    l = len(matrix)
    z = (l if l % 2 == 0 else l + 1) / 2
    for i in range(0, z):
        t = matrix[i][i]
        matrix[i][i] = matrix[l - 1 - i][l - 1 - i]
        matrix[l - 1 - i][l - 1 - i] = t

        t = matrix[l - 1 - i][i]
        matrix[l - 1 - i][i] = matrix[i][l - 1 - i]
        matrix[i][l - 1 - i] = t
    return matrix


def swapDiagonals(matrix):
    l = len(matrix)
    z = (l if l % 2 == 0 else l + 1) / 2
    for i in range(0, l):
        t = matrix[i][i]
        matrix[i][i] = matrix[i][l - 1 - i]
        matrix[i][l - 1 - i] = t
    return matrix


def drawRectangle(canvas, rectangle):
    w = rectangle
    p = [(w[1], w[0]), (w[1], w[2]), (w[3], w[0]), (w[3], w[2])]

    for r in range(len(canvas)):
        for c in range(len(canvas[r])):
            if (r, c) in p:
                canvas[r][c] = '*'
            elif r in [i[0] for i in p] and w[0] < c < w[2]:
                canvas[r][c] = '-'
            elif c in [i[1] for i in p] and w[1] < r < w[3]:
                canvas[r][c] = '|'

    return canvas

