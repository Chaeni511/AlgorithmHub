class Solution {
    static int r;
    
    public int solution(int[][] triangle) {
        int[][] dp = new int[triangle.length][];
        Boolean flag = true;
        
        for (int i = triangle.length-1; i >= 0; i--) {
            
            int[] tmp = new int[i+1];
            if (flag) {
                for (int j = 0; j <= i; j++) {
                    tmp[j] = triangle[i][j];
                    flag = false;
                }
                
            } else {
                for (int j = 0; j <= i; j++) {
                    if (dp[i+1][j] > dp[i+1][j+1]) {
                        tmp[j] = triangle[i][j] + dp[i+1][j];
                    } else {
                        tmp[j] = triangle[i][j] + dp[i+1][j+1];
                    }
                }
            }
            dp[i] = tmp;
        }
        // return new int[10];
       
        return dp[0][0];
    }
    
}