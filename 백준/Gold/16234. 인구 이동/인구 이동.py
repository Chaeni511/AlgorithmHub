from collections import deque


def bfs():
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(A[x][y] - A[nx][ny]) <= R:
                visited[nx][ny] = 1
                Q.append((nx, ny))
                union.append((nx, ny))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
res = 0
while True:
    flag = 0
    # 연합국 구하기
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            Q = deque()
            union = []
            if not visited[i][j]:
                visited[i][j] = 1
                union.append((i, j))
                Q. append((i, j))
                bfs()

                # 연합이 있으면 인구 이동
                if len(union) > 1:
                    flag = 1
                    temp = 0
                    cnt = 0
                    for x, y in union:
                        temp += A[x][y]
                        cnt += 1
                    for x, y in union:
                        A[x][y] = temp // cnt


    if not flag:
        break
    else:
        res += 1

print(res)


