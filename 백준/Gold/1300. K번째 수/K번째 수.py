import sys

N, k = int(sys.stdin.readline()), int(sys.stdin.readline())

start, end = 1, k

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for i in range(1, N + 1):
        tmp += min(mid // i, N)

    if tmp >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)