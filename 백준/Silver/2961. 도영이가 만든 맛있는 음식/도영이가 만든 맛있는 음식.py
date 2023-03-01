N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 987654321
for i in range(1 << N):
    temp = []
    for j in range(N):
        if i & (1 << j):
            temp.append(j)
    if temp:
        s = 1
        b = 0
        for t in temp:
            s *= arr[t][0]
            b += arr[t][1]
        res = min(abs(s-b), res)
print(res)