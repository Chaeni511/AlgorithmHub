class Solution {
    public int solution(int[] arr) {
        int ans = 1;
        for (int i = 0; i < arr.length; i++) {
            for (int j = Math.max(ans, arr[i]); j < ans * arr[i] +1; j++){
                if (j % ans == 0 && j % arr[i] == 0) {
                    ans = j;
                    break;
                }
            }
                        
        }
        return ans;
        
    }
}