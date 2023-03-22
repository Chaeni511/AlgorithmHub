from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
res = 987654321
for comb in combinations([_ for _ in range(N)], N//2):
    s1 = []
    s2 = []
    for i in range(N):
        if i in comb:
            s1.append(i)
        else:
            s2.append(i)
    res1 = res2 = 0
    for i in s1:
        for j in s1:
            if i != j:
                res1 += S[i][j]
    for i in s2:
        for j in s2:
            if i != j:
                res2 += S[i][j]
    res = min(res, abs(res1-res2))
print(res)