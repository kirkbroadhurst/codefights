from collections import Counter

def runnersMeetings(startPosition, speed):
    # zip together, sort by speed, then separate

    items = sorted(zip(speed, startPosition))
    speeds = [i[0] for i in items]
    positions = [60*i[1] for i in items]

    c = count_same(positions, 0)

    while positions != sorted(positions):
        positions = move(positions, speeds)
        c = count_same(positions, c)

    return c

    '''
    c = 0
    i = len(startPosition)
    r = sorted(zip(speed, [60 * s for s in startPosition]), key=lambda x: x[1])
    print r

    c = countSame(r, c)

    j = 0
    while str(r) != str(sorted(r)) and j < 100:  #
        c = countSame(r, c)

        r = sorted([(i, i + z) for (i, z) in r])
        j += 1

        print sorted(r), r, str(r) != str(sorted(r))
        if j % 10 == 0:
            print sorted(r), r, j, str(r) != str(sorted(r))
            #

    return c
    '''


def move(positions, speeds):
    return map(lambda x: x[0]+x[1], zip(positions, speeds))


def count_same(positions, c):
    vals = Counter(positions)
    return max(c, max(vals.values()))

def countSame(items, c):
    print 'count', items, c
    vals = Counter([s[1] for s in items])
    print vals
    c = max(c, max(vals.values()))
    print items, c
    return c

def test_count():
    assert countSame([(10, 60), (10, 60), (10, 60), (10, 120), (10, 120)], 0) == 3

positions = [1, 2, 3]
speeds = [1, 1, 1]

items = sorted(zip(speeds, positions))
speeds = [i[0] for i in items]
positions = [60 * i[1] for i in items]

c = count_same(positions, 0)
print c
while positions != sorted(positions):
    positions = move(positions, speeds)

    c = count_same(positions, c)
    print positions, c
pass


#print runnersMeetings(positions, speeds)

#items = [(10, 60), (10, 60), (10, 60), (10, 120), (10, 120)]
#print countSame(items, 0)
#vals = Counter([s[1] for s in items])
#print vals

#print move(positions, speeds)