import sys
N = int(sys.stdin.readline())
skill = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
player = list(range(N))


result = 98754321

for i in range(1<<N):
    team1 = []
    t1 = 0
    team2 = []
    t2 = 0
    for j in range(N):
        if i & (1<<j):
            team1.append(j)
    if len(team1) == N//2:
        for p in player:
            if p not in team1:
                team2.append(p)
        
        for i in team1:
            for j in team1:
                t1 += skill[i][j]
        
        for i in team2:
            for j in team2:
                t2 += skill[i][j]
        if abs(t1 - t2) < result:
            result = abs(t1 - t2)
print(result)