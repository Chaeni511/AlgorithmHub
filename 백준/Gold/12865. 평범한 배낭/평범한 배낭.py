N, K = map(int, input().split())
arr = [(0,0)]
dp = [[0] * (K+1) for _ in range(N+1)]
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = arr[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(dp[N][K])

