m = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]

def boxBlur(image):
    j_ = len(image)
    i_ = len(image[0])

    result = []
    for j in range(1, j_-1):
        row = []
        for i in range(1, i_-1):
            row.append(sum([x for r in image[j-1:j+2] for x in r[i-1:i+2]])/9)
        result.append(row)

    return result


print boxBlur(m)