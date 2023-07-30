import sys
sys.setrecursionlimit(10**6)


def dfs(s):
    for i in graph[s]:
        if not visited[i]:
            visited[i] = s
            dfs(i)


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(1)

for i in range(2, n+1):
    print(visited[i])
