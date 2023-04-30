import sys

n, m = map(int, sys.stdin.readline().split())
memo = {}

for i in range(n):
    memo[sys.stdin.readline().rstrip()] = True

for _ in range(m):
    for i in list(sys.stdin.readline().rstrip().split(',')):
        if i in memo.keys() and memo[i]:
            memo[i] = False
            n -= 1
    print(n)
