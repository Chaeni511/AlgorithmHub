from collections import deque


def bfs():
    while tomatoes:
        i, j, c = tomatoes.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                tomatoes.append((ni, nj, c+1))
        if not tomatoes:
            return c


di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

M, N = map(int, input().split())    # 가로, 세로
arr = [list(map(int, input().split())) for _ in range(N)]
tomatoes = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomatoes.append((i, j, 0))

cnt = bfs()
flag = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt = -1
            break
print(cnt)