N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(N):
    if arr[i][0] == K:
        print(arr.index(arr[i]))
        break