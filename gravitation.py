input = ["#..##",
        ".##.#",
        ".#.##",
        "....."]


def gravitation(rows):
    cols = pivot_and_reverse(rows)
    stopped = is_motionless(cols)
    while not any(stopped):
        [drop(c) for c in cols]
        stopped = is_motionless(cols)

    return stopped


def pivot_and_reverse(rows):
    l = len(rows[0])
    return [[r[x] for r in rows][::-1] for x in range(l)]


def is_motionless(cols):
    check = lambda x: not any([x[i] == '.' and x[i + 1] == '#' for i in range(len(x) - 1)])
    return [i for (i, c) in enumerate(cols) if check(c)]


def drop(c):
    if '.' in c:
        del c[c.index('.')]
        c.append('.')
    return c



'''
print is_motionless(cols)

check = lambda x: not any([x[i] == '.' and x[i+1] == '#' for i in range(len(x)-1)])
print check(['.', '#'])
print check(['#', '.'])
print check(['.', '.'])
print check(['#', '#'])
'''

cc = pivot_and_reverse(input)
print cc

print is_motionless(cc)
[drop(c) for c in cc]

print is_motionless(cc)

