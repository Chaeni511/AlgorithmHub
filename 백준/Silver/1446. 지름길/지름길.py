N, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
road = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        road[i] = min(road[i-1] + 1, road[i])
    for s, e, d in arr:
        if i == s and e <= D and road[i]+d < road[e]:
            road[e] = road[i] + d

print(road[D])