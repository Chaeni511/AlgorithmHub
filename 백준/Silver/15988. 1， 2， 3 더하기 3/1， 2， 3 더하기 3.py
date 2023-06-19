T = int(input())
N = [int(input()) for _ in range(T)]
n = max(N)
dp = [0] * (n+1)

for i in range(T):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

for i in range(4, n + 1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for n in N:
    print(dp[n])
