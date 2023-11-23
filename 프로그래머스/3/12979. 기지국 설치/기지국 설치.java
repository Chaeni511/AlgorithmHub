import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        
        int coverage = 2 * w + 1;
        
        int start = 0;
        
        for (int i = 0; i < stations.length; i++) {
            
            int s = stations[i] - w -1;
                
            if (start < s) {
                // answer += Math.ceil((s-start)/coverage);
                answer += (s-start)/coverage;
                if ((s-start) % coverage > 0) {
                    answer++;
                }                    
            } 
            start = stations[i] + w;
            
        }

        answer += Math.ceil((n-start)/coverage);
        
        // answer += (n-start)/coverage;
        if ((n-start) % coverage > 0) {
            answer++;
        }
        return answer;
    }
}