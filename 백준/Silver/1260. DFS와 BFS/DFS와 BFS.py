def dfs(v):
    if visited[v]:
        return
    print(v, end=' ')
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)


import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N+1):
    arr[i].sort()

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
Q = deque([V])
visited[V] = True
while Q:
    temp = Q.popleft()
    print(temp, end=' ')
    for i in arr[temp]:
        if not visited[i]:
            Q.append(i)
            visited[i] = True

# stack = [V]
# rear = 0
# while rear < len(stack):
#     if not visited[stack[rear]]:
#         visited[stack[rear]] = True
#         print(stack[rear], end=' ')
#         for i in arr[stack[rear]]:
#             if not visited[i]:
#                 stack.append(i)
#         rear += 1