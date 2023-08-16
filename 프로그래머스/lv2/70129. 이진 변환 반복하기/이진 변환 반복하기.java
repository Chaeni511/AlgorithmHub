import java.util.*;

class Solution {

    public int[] solution(String s) {
        
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {

            int len = 0;
            
            for (int i=0; i < s.length(); i++) {
                
                if (s.charAt(i) == '0') {
                    answer[1]+= 1;
                
                } else {
                    len++;
                }
            }

            s = Integer.toBinaryString(len);
            answer[0]+= 1;
         
        }

        return answer;
    }
}