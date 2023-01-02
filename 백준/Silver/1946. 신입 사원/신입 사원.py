T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    temp = arr[0][1]
    res = 1
    for i in range(1, N):
        if arr[i][1] <= temp:
            temp = arr[i][1]
            res += 1
    print(res)
