import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
arr.sort(reverse=True)
weight = []
for i in range(N):
    weight.append(arr[i] * (i + 1))

print(max(weight))