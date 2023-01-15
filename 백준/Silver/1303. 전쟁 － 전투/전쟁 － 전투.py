def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == team:
            cnt += 1
            dfs(nx, ny)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
w = b = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            team = arr[i][j]
            cnt = 1
            dfs(i, j)
            if team == 'W':
                w += cnt**2
            else:
                b += cnt**2

print(w, b)
