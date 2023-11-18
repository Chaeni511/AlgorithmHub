class Solution {
    // public int[][] solution(int m, int n, int[][] puddles) {
    public int solution(int m, int n, int[][] puddles) {
        int[][] map = new int[n+1][m+1];
        map[1][1] = 1;
        
        for (int[] puddle: puddles) {
            map[puddle[1]][puddle[0]] = -1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (map[i][j] != -1) {
                    if (map[i-1][j] != -1) {
                        map[i][j] += map[i-1][j];
                    }
                    if (map[i][j-1] != -1) {
                        map[i][j] += map[i][j-1];
                    }
                    map[i][j] %= 1000000007;
                    // if (map[i-1][j] > 0 && map[i][j-1] > 0) {
                    //     map[i][j] = map[i-1][j] + map[i][j-1];                   
                    // } else if (map[i-1][j] > 0) {
                    //     map[i][j] = map[i-1][j];
                    // } else if (map[i][j-1] > 0) {
                    //     map[i][j] = map[i][j-1];
                    // }
                }
            }
        }
        // return map;
        return map[n][m];
    }
}