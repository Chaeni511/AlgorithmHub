def travel(s, e, c):
    global res
    if c > res:
        return

    if 0 not in visited:
        if expense[s][e]:
            c += expense[s][e]
            res = min(res, c)

    for j in range(N):
        if visited[j] != -1 and not visited[j] and expense[s][j]:
            visited[j] = 1
            travel(j, e, c + expense[s][j])
            visited[j] = 0


N = int(input())
expense = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
res = 987654321

for i in range(N):
    visited[i] = -1
    travel(i, i, 0)
    visited[i] = 0

print(res)
