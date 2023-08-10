import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int work: works) {
            pq.add(work);
        }
        
        for (int i = 0; i < n; i++) {
            pq.add(pq.poll() - 1);
        }
        
        for (int i : pq) {
            if (i > 0) {
                answer += i * i;
            }
        }
        return answer;
    }
}