class Solution {
    public long solution(int n) {

        int[] jump = new int[n+1];
        jump[0] = 1;
        jump[1] = 1;
        
        for (int i = 2; i < n+1; i++) {
            
            // if (i == 1){
            //     continue;
            // }
            
            jump[i] = (jump[i-1] + jump[i-2])%1234567;
        }
        return jump[n];
    }
}