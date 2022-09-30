import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
n = list(permutations([e for e in range(1, N+1)], M))
for i in range(len(n)):
    print(' '.join(map(str, n[i])))