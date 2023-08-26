class Solution {
    
    public int solution(int n, int a, int b) {
        
        int answer = 1;

        while (Math.abs(a - b) != 1 || Math.max(a, b) % 2 != 0) {
            answer += 1;
            a = game(a);
            b = game(b);
            
            if (a % 2 == 0 && a - 1 == b) {                    
                break;

            } else if (a % 2 == 1 && a + 1 == b) {
                break;
            }
        }

        return answer;
    }
    
    
    private int game (int i) {
        
        int res = i/ 2;
        
        if (i % 2 == 1) {
            res += 1;
        } 
        
        return res;
    }
    
    private Boolean check (int p1, int p2) {
        
        if (p1 % 2 == 0) {
            
            if (p1 - 1 == p2) {
                return true;
            }
            
        } else {
            
            if (p1 + 1 == p2) {
                return true;
            }
        }
        
        return false;
    }
}