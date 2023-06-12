from collections import deque
n, m = map(int, input().split())
glacier = [list(map(int, input().split())) for _ in range(n)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

q = deque()


def bfs(x, y):
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for d in range(4):
            nx, ny = x + di[d], y + dj[d]
            if 0 <= nx < n and 0 <= ny < m:
                if glacier[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif glacier[nx][ny] == 0:
                    count[x][y] += 1


one = True
year = 0

while one:
    g = 0
    visited = [[0] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if glacier[i][j] and not visited[i][j]:
                bfs(i, j)
                g += 1

    for i in range(n):
        for j in range(m):
            glacier[i][j] -= count[i][j]
            if glacier[i][j] < 0:
                glacier[i][j] = 0

    if g == 0:
        year = 0
        break
    if g >= 2:
        break

    year += 1

print(year)
