from itertools import combinations

N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
res = 0
for r in range(1, N+1):
    for comb in combinations(range(N), r):
        tempL = 0
        for i in comb:
            tempL += L[i]
        if tempL < 100:
            tempJ = 0
            for i in comb:
                tempJ += J[i]
            if tempJ > res:
                res = tempJ
print(res)