import sys
sys.setrecursionlimit(10**5)

def dfs(node, cost):
    for adj, w in tree[node]:
        if visited[adj] == -1:
            visited[adj] = w + cost
            dfs(adj, visited[adj])


N = int(sys.stdin.readline())
tree = {}
visited = [-1] * (N + 1)

visited[1] = 0

for i in range(1, N+1):
    tree[i] = []

for _ in range(N-1):
    p, c, w = map(int, sys.stdin.readline().strip().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[start] = 0

dfs(start, 0)

print(max(visited))