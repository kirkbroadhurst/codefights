

def boxesPacking(length, width, height):
    t = sorted([sorted(q) for q in zip(length, width, height)])
    print t
    print [[(t[i][j] < t[i+1][j]) for j in range(3)] for i, tt in enumerate(t[1:])]
    return all([t[i][j] < t[i+1][j] for j in range(3) for i, tt in enumerate(t[1:])])

'''
l = [1, 3, 2]
w = [1, 3, 2]
h = [1, 3, 2]
'''

# l = w = h = [1,1]

l = [5, 7, 4, 1, 2]
w = [4, 10, 3, 1, 4]
h = [6, 5, 5, 1, 2]

print boxesPacking(l, w, h)