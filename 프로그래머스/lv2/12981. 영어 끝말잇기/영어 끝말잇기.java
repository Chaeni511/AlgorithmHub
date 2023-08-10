import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        
        List<String> check = new ArrayList();
        
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
    
            if ((i != 0 && words[i-1].charAt(words[i-1].length()-1) != word.charAt(0)) || check.contains(word)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
                
            } else {
                check.add(word);
            }
        }

        return answer;
    }
}