import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        Integer minimum = Integer.MAX_VALUE;
        Integer maximum = Integer.MIN_VALUE;
        String[] strings = s.split("\\s");
        
        for (String string : strings) {
            int num = Integer.parseInt(string);
            if (num < minimum){
                minimum = num;
            }
            if (num > maximum) {
                maximum = num;
            }
        }
        return Integer.toString(minimum) + " " + Integer.toString(maximum);
    }
}