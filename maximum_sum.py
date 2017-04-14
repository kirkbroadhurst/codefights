def maximumSum(arr, queries):
    qq = [range(q[0], 1+q[1]) for q in queries]
    flat = [x for y in qq for x in y]

    print qq, flat

    from collections import Counter
    items = Counter(flat)
    print items

    cc = sorted(items.values(), reverse = True)
    vals = sorted(arr, reverse = True)

    print cc, vals

    return sum([a*b for (a,b) in zip(cc, vals)])


a = [4, 2, 1, 6, 5, 7, 2, 4]
q = [[1, 6],  [2, 4],  [3, 6],  [0, 7],  [3, 6],  [4, 4], 
     [5, 6],  [5, 6],  [0, 1],  [3, 4]]


# a = [2,1,2]
# q = [[0,1]]

print maximumSum(a, q)