import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [[num for num in nums] for _ in range(2)]
#
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + nums[i], dp[0][i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + nums[i])
    
print(max(max(dp[0]), max(dp[1])))
