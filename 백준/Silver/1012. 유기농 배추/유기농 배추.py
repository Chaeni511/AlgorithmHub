import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(sys.stdin.readline())
for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, sys.stdin.readline().split())
        arr[n][m] = 1

    cnt = 0
    stack = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = 0
                stack.append((i, j))
                while stack:
                    x, y = stack.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                            arr[nx][ny] = 0
                            stack.append((nx, ny))
                cnt += 1

    print(cnt)