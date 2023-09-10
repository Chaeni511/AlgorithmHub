import java.util.*;

class Solution {
    public int solution(String S) {
        int answer = 0;
        
        for(int i = 0; i < S.length(); i++){
            int s = i;
            
            boolean res;
            
            if (i == 0) {
                res = spin(S); 
            } else {
                res = spin(S.substring(s, S.length()) + S.substring(0, s));
            }
            
            if(res) {
                answer++;
            }
         }
        return answer;
    } 
    
    private boolean spin(String s){
        
        Deque<Character> dq = new ArrayDeque<>();   
        
        for (int i = 0; i < s.length(); i++){
            
            if (dq.isEmpty()) {
                dq.add(s.charAt(i));   
                continue;
            }
            
            if((s.charAt(i) == ']' && dq.peekLast() == '[')
              || (s.charAt(i) == ')' && dq.peekLast() == '(')
              || (s.charAt(i) == '}' && dq.peekLast() == '{')
            ){
                dq.pollLast();
            } else {
                dq.add(s.charAt(i));
            }
    
        }
        if (dq.isEmpty()) {
            return true;
        }
        return false;
        
    }
}