import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long max = (long) times[times.length -1] *n;
        long min = 1;
        long answer = max;
            
        
        while (min <= max){
            long avg = (min + max) / 2;
            long tmp = 0;
            
            for (int i = 0; i < times.length; i++) {
                tmp += avg / times[i];
                
                if (tmp >= n) {
                    break;
                }
            }
            
            if (tmp < n) {
                min = avg + 1;
            } else {
                answer = Math.min(answer, avg);
                max = avg -1;
            }
        }
        return answer;
        
    }
}