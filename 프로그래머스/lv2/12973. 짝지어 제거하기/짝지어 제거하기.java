import java.util.*;

class Solution {
    public int solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            
            if (stack.empty()) {
                stack.push(s.charAt(i));
                
            } else {
                
                if (stack.peek() == s.charAt(i)) {
                    stack.pop();    
                    
                } else {
                    stack.push(s.charAt(i));
                }
            }
        }
        
        // return stack;
        if (stack.empty()) {
            return 1;
        } else {
            return 0;
        }
    }
    
    
    private int check(String s) {
        Stack<Character> stack = new Stack<>();
        
    // private String check(String s) {
        String tmp = "";
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                // String tmp = s.substring(0,i) + s.substring(i+2);
                tmp = s.substring(0,i) + s.substring(i+2);
                
                if (tmp.length() == 0) {
                    return 1;
                } else {
                    return check(tmp);
                }
            }
        }
        
        return 0;
    }
}