import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        
        int size = (int) (right - left + 1);
        
        int[] arr = new int[size];
        
        for (long i = left; i <= right; i++) {
            int idx = (int) (i-left);
            int tmp = (int) Math.max(i/n + 1, i%n + 1);
            arr[idx] = tmp;
            
        }
        
        return arr;
    }
}