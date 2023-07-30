import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        
        int s = 0;
        int e = people.length -1;
        int tmp = people[e];
        
        while (s < e) {
            if (tmp + people[s] <= limit) {
                tmp += people[s];
                s += 1;
            } else {
                answer += 1;
                e -= 1;
                tmp = people[e];
            }
        }
        
        return answer + 1;
    }
}