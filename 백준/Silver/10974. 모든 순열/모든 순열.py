import sys
def perm(n, k):
    if k == N:
        print(*p)
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            p[k] = a[i]
            perm(n, k + 1)
            visited[i] = 0


N = int(sys.stdin.readline())
a = list(range(1, N+1))
p = [0] * N
visited = [0] * N
perm(N, 0)