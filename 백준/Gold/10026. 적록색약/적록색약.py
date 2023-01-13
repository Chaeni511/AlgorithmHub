import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = 1

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == color and visited[nx][ny] == 0:
            dfs(nx, ny)


def dfs_cb(x, y):
    visited_cb[x][y] = 1

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if color == 'B':
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'B' and visited_cb[nx][ny] == 0:
                dfs_cb(nx, ny)
        else:
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 'B' and visited_cb[nx][ny] == 0:
                dfs_cb(nx, ny)


n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited_cb = [[0]*n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = 0
res_cb = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            res += 1
            color = arr[i][j]
            dfs(i, j)

        if visited_cb[i][j] == 0:
            res_cb += 1
            color = arr[i][j]
            dfs_cb(i, j)

print(res, res_cb)
