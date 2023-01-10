def bfs(x, y):
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        i, j = stack.pop()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > k and not visited[ni][nj]:
                visited[ni][nj] = 1
                stack.append((ni, nj))


di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
temp = 0
res = 0

# 최대 강수량 구하기
max_rain = 0
for i in range(N):
    max_rain = max(max(arr[i]), max_rain)

for k in range(max_rain):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visited[i][j]:
                cnt += 1
                bfs(i, j)
    if cnt > res:
        res = cnt
print(res)