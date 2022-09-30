import sys
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    # airline = [[] for _ in range(N + 1)]

    airline = [ list(sys.stdin.readline()) for _ in range(M)]
    print(N - 1)