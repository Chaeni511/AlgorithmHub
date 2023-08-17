import sys
sys.setrecursionlimit(1000000)


def dfs(x, y):
    visited[x][y] = 1
    res = 1

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
            res += dfs(nx, ny)

    return res


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, sys.stdin.readline().strip().split())    # col, row
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
width = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            width = max(width, dfs(i, j))

print(cnt)
print(width)
