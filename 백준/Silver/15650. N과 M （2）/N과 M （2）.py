import sys
def combination(result):
    if len(result) == M:
        return print(' '.join(map(str, result)))

    if result:
        start = result[-1]+1
    else:
        start = 1

    for i in range(start, N+1):
        combination(result+[i])


N, M = map(int, sys.stdin.readline().split())
combination([])