class Solution {
    public int solution(int n) {
        
        int[] dp = new int[n+1];
        
        dp[0] = 0;
        dp[1] = 1;
        
        int answer = 0;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        // return dp;
        return dp[n];
    }
}