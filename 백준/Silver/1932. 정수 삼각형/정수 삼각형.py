N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(n+1) for n in range(N)]
dp[0][0] = triangle[0][0]

for i in range(N):
    for j in range(len(dp[i])):
        if i+1 < N:
            dp[i+1][j] = max(triangle[i+1][j] + dp[i][j], triangle[i+1][j], dp[i+1][j])
            dp[i+1][j+1] = max(triangle[i + 1][j+1] + dp[i][j], triangle[i + 1][j+1], dp[i + 1][j+1])

print(max(dp[N-1]))
