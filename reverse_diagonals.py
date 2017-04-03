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


