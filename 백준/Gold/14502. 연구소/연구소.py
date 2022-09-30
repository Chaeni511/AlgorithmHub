import sys
from itertools import combinations


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread(x, y):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if map[nx][ny] == 0:
                map[nx][ny] = 2
                spread(nx, ny)


def count():
    global result
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                cnt += 1
    if cnt > result:
        result = cnt


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


empty = []      # 빈 공간의 좌표를 담는 리스트
virus = []      # 바이러스 좌표를 담는 리스트
wall = []       # 벽의 좌표를 담는 리스트
result = 0      # 최종 정답(빈 칸의 개수)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
        else:
            wall.append((i, j))

choose_empty = combinations(empty, 3)

for choice in choose_empty:
    map = [[0] * M for _ in range(N)]
    for x, y in choice:
        map[x][y] = 1

    for x, y in wall:
        map[x][y] = 1
    for x, y in virus:
        map[x][y] = 2

    for x, y in virus:
        spread(x, y)
    count()
print(result)

