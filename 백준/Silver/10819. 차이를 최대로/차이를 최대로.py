from itertools import permutations
N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(N-1):
    res += abs(A[i] - A[i+1])

for arr in permutations(A, N):
    # print(arr)
    temp = 0
    for i in range(N - 1):
        temp += abs(arr[i] - arr[i + 1])
    res = max(res, temp)

print(res)
