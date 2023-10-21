import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
        Integer[] a = Arrays.stream(A).boxed().toArray(Integer[]::new);
        Integer[] b = Arrays.stream(B).boxed().toArray(Integer[]::new);
        
        Arrays.sort(a, Collections.reverseOrder());
        Arrays.sort(b, Collections.reverseOrder());        
       
        int idx = -1;
        
        for (int i = 0; i < a.length; i++) {
            for (int j = idx + 1; j < b.length; j++) {
                if (a[i] < b[j]){
                    answer++;
                    idx = j;
                    break;
                }
            }
        }
        
        return answer;
    }
}