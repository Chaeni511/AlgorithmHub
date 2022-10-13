import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
result = 0

for i in range(N):
    if A[i] - B >= 0:
        A[i] -= B
    else:
        A[i] = 0
    result += 1

for a in A:
        if a % C == 0:
            result += a//C
        else:
            result += a//C + 1
    
print(result)
