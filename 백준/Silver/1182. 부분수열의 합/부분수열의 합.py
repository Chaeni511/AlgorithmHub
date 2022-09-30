import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(1, N+1):
    n = list(combinations(arr, i))
    for j in range(len(n)):
        if sum(n[j]) == S:
            cnt += 1
print(cnt)