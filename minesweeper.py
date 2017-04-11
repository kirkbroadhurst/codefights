m = [[True,False,False],
 [False,True,False],
 [False,False,False]]

def minesweeper(matrix):
    j_ = len(matrix)
    i_ = len(matrix[0])

    result = []
    for j in range(j_):
        row = []
        for i in range(i_):
            row.append(sum([1 if x else 0 for r in matrix[max(0, j-1):min(j_, j+2)]
                            for x in r[max(0, i-1):min(i_, i+2)]]) - (1 if matrix[j][i] else 0))
        result.append(row)

    return result


print minesweeper(m)