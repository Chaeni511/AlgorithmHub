from collections import deque


def bfs():
    while Q:
        x, y = Q.popleft()
        if (x, y) == (r2, c2):
            break

        for d in range(6):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx, ny))
    return visited[r2][c2]


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[-1] * N for _ in range(N)]
Q = deque()
visited[r1][c1] = 0
Q.append((r1, c1))
print(bfs())