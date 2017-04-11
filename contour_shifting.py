#m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
#m = [[238,239,240,241,242,243,244,245]]
m = [[238], [239], [240], [241],[242],[243],[244],[245]]

def contoursShifting(matrix):
    y = len(matrix)
    x = len(matrix[0])

    i_ = (1+min(x,y))/2

    for i in range(i_):
        contour = getContour(matrix, i)
        values = getValues(matrix, contour)
        if i%2 == 0:
            values.insert(0, values[-1])
            del values[-1]
        else:
            values.append(values[0])
            del values[0]
        putValues(matrix, contour, values)

    return matrix


def getValues(matrix, contour):
    return [matrix[c[1]][c[0]] for c in contour]


def putValues(matrix, contour, values):
    for c, v in zip(contour, values):
        matrix[c[1]][c[0]] = v
    return matrix


def getContour(matrix, i):
    y = len(matrix)
    x = len(matrix[0])

    print i

    if i == y-i-1:
        print 'i == y-i-1'
        return [(z, i) for z in range(i, x-i)]

    if i == x-i-1:
        print 'i == x-i-1'
        return [(x-i-1, z) for z in range(i, y-i)]


    result = []
    result += [(z, i) for z in range(i, x-i)]
    result += [(x-i-1, z) for z in range(i+1, y-i)]
    result += [(z, y-i-1) for z in range(x-i-2, i-1, -1)]
    result += [(i, z) for z in range(y-i-2, i, -1)]

    return result


print contoursShifting(m)
