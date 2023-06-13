import java.util.*;

class Solution {
    
    public int solution(int x, int y, int n) {
        
        int answer = 0;
        HashSet<Integer> list = new HashSet<>();
        list.add(x);
        HashSet<Integer> temp = null;
        
        while (!list.isEmpty()) {
            
            if (list.contains(y)) {
                return answer;
            }    
            
            temp = new HashSet<>();
            
            for (int t: list) {
                if (t + n <= y) {
                    temp.add(t + n);
                }
                if (t *2 <= y) {
                    temp.add(t * 2);
                }
                if (t *3 <= y) {
                    temp.add(t * 3);
                }
            }
            
            list = temp;
            answer++;
        }
        
        return -1;
    }
    
}