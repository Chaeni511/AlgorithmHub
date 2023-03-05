from collections import deque
import sys
f = sys.stdin.readline

def bfs():
    while Q:
        s = Q.popleft()
        for e in arr[s]:
            if not visited[e]:
                distance[e] = distance[s] + 1
                visited[e] = True
                Q.append(e)


N, M, K, X = map(int, f().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, f().split())
    arr[s].append(e)

distance = [0] * (N+1)
visited = [False] * (N+1)
Q = deque()
visited[X] = True
Q.append(X)

bfs()

flag = True
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        flag = False
if flag:
    print(-1)