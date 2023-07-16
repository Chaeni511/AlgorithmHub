from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1

    melt = []

    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if not arr[ni][nj]:
                    q.append((ni, nj))
                else:
                    melt.append((ni, nj))

    for i, j in melt:
        arr[i][j] = 0

    return len(melt)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
left_cheeze = 0

for n in range(N):
    left_cheeze += sum(arr[n])

while True:
    visited = [[0] * M for _ in range(N)]
    melted_cheeze = bfs()
    left_cheeze -= melted_cheeze
    if not left_cheeze:
        print(cnt)
        print(melted_cheeze)
        break
    cnt += 1
