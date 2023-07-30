import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strings = s.split("");

        for (int i = 0; i < strings.length; i++) {
            
            if (i == 0 || strings[i-1].isBlank()) {
                strings[i] = strings[i].toUpperCase();
                
            } else if (Character.isUpperCase(s.charAt(i))) {
                strings[i] = strings[i].toLowerCase();
            }
        }
        
        return String.join("", strings);
    }
}