import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p = sys.stdin.readline().rstrip().split()

    myset= set()

    if p[0] == 'add':
        myset.add(p[1])

    if p[0] == 'remove':
        if p[1] in myset:
            myset.remove(p[1])

    if p[0] == 'check':
        if p[1] in myset:
            print(1)
        else:
            print(0)

    if p[0] == 'toggle':
        if p[1] in myset:
            myset.remove(p[1])
        else:
            myset.add(p[1])

    if p[0] == 'all':
        myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    if p[0] == 'empty':
        myset = set()
    