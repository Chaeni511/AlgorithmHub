N = int(input())
players = ['SK', 'CY']
dp = [-1] * 1001
dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, N+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1
print(players[dp[N]])
