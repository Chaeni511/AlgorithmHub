# 내 코드
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)

n, k = map(int, input().split())
visited = [0] * 100001

bfs()