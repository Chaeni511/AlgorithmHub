from collections import deque


def bfs():
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                Q.append((nx, ny))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

M, N = map(int, input().split())    # 세로, 가로
arr = [list(map(int, input())) for _ in range(M)]
Q = deque()

for i in range(N):
    if not arr[0][i]:
        arr[0][i] = 2
        Q.append((0, i))
bfs()

for i in range(N):
    if arr[M-1][i] == 2:
        print('YES')
        break
else:
    print('NO')