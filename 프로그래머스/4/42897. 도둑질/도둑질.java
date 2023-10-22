class Solution {
    public int solution(int[] money) {
        int answer = 0;
        // int[] tmp = {1000,1,0,1,2,1000,0};
        int[][] houses = {makeDp(0, money), makeDp(1, money)};
        // int[][] houses = {makeDp(0, tmp), makeDp(1, tmp)};
        // return houses;
        for (int i = 0; i < 2; i++) {
            // for (int h = 2 ; h < tmp.length; h++) {
            for (int h = 2 ; h < money.length; h++) {
                houses[i][h] = Math.max(houses[i][h-1], houses[i][h-2] + houses[i][h]);
            }
        }

        for (int[] house: houses) {
            for (int h: house) {
                if (h > answer) {
                    answer = h;
                }
            }
        }
        return answer;
    }
    
    private int[] makeDp(int n, int[] money) {
        int[] dp = new int[money.length];
        
        if (n == 0) {
            for (int i = 0; i < money.length-1; i++) {
                dp[i+1] = money[i];
            }
        } else {
            for (int i = 1; i < money.length; i++) {
                dp[i] = money[i];
            }
        }
        
        return dp;   
    }
    
}