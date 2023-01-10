from collections import deque

def bfs(i,j):
    deq = deque()
    deq.append((i,j))
    visited[i][j] = 1
    while deq:
        i, j = deq.popleft()

        if i == ei and j == ej:
            return visited[i][j] - 1

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                deq.append((ni, nj))

t = int(input())
for tc in range(t):
    l = int(input())
    si, sj = map(int,input().split())
    ei, ej = map(int,input().split())

    di = [-2,-1,1,2,2,1,-1,-2]
    dj = [1,2,2,1,-1,-2,-2,-1]

    visited = [[0] * l for _ in range(l)]
    print(bfs(si, sj))