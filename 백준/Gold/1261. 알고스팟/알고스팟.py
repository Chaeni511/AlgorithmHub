import sys
from collections import deque


def dijkstra():

    dq = deque()
    dq.append((0, 0))
    dij[0][0] = 0

    while dq:
        i, j = dq.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < N and 0 <= nj < M:
                if dij[ni][nj] == -1:
                    if maze[ni][nj] == 0:
                        dij[ni][nj] = dij[i][j]
                        dq.appendleft((ni, nj))
                    else:
                        dij[ni][nj] = dij[i][j] + 1
                        dq.append((ni, nj))
                        

M, N = map(int, sys.stdin.readline().strip().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

hq = []
dij = [[-1] * M for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

dijkstra()

print(dij[N-1][M-1])
