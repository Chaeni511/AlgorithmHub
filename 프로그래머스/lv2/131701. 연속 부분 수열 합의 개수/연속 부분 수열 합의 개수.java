import java.util.*;

class Solution {
    public int solution(int[] elements) {
        
        Set<Integer> subsequence = new HashSet();
        
        int[] dp = new int[elements.length];
        
        for (int i = 0; i < elements.length; i++) {
            dp[i] = elements[i];
            subsequence.add(elements[i]);   
        }
        
        for (int i = 1; i < elements.length; i++) {
            for (int j = 0; j < elements.length; j++) {
                dp[j] += elements[(j+i) % elements.length];
                subsequence.add(dp[j]);
            }
            
        }
        
        return subsequence.size();
    }
}