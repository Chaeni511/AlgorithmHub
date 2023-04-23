import sys
N, M = map(int, sys.stdin.readline().split())
title = []

for _ in range(N):
    x, y = sys.stdin.readline().split()
    title.append([x, int(y)])

for _ in range(M):

    num = int(sys.stdin.readline())
    s, e = 0, N-1

    while s <= e:
        m = (s+e)//2
        if num > title[m][1]:
            s = m + 1
        else:
            e = m -1
    print(title[e+1][0])