import sys
T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = [e for e in range(N)]
    importance = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    while len(arr) > 0:
        j = importance[arr[0]]
        for i in range(1, len(arr)):
            if importance[arr[i]] > j:
                arr.append(arr.pop(0))
                break
        else:
            m = arr.pop(0)
            cnt += 1
            if m == M:
                print(cnt)
                break
