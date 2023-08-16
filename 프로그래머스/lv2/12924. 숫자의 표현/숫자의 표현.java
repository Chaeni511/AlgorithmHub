class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i++) {
            answer += check(i, n);       
        }
        
        return answer;
    }
    
    
    private int check(int start, int n) {
    
        int tmp = 0;
        
        for (int s = start; s <= n; s++) {
            
            tmp += s;
            
            if (tmp == n) {
                return 1;
                
            } else if (tmp > n) {
                return 0;
            }
        }
        
        return 0;
    }
}