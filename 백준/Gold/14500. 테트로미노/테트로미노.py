def dfs(x, y, k, c):    #x,y 좌표, 깊이, 총
    global res
    if k == 3:
        res = max(res, c)
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, k + 1, c + arr[nx][ny])
            visited[nx][ny] = 0


from itertools import combinations
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
res = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0
        for c in combinations(range(4), 3):
            temp = arr[i][j]
            for cc in c:
                ni, nj = i + dx[cc], j + dy[cc]
                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]
                else:
                    break
            res = max(res, temp)

print(res)