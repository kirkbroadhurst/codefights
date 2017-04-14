def sortByHeight(a):
    items = sorted([x for x in a if x != -1])

    for i, z in enumerate(a):
        if z == -1:
            continue
        a[i] = items[0]
        del items[0]

    return a


aa = [-1, 150, 190, 170, -1, -1, 160, 180]

print sortByHeight(aa)