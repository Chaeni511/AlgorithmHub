import java.util.*;

class Solution {
    public static int bubleSort(List<Integer> valArr, int c) {
        for(int i = 0; i < valArr.size(); i++) {
            for(int j = 0 ; j < valArr.size() - i - 1 ; j++) {
                if(valArr.get(j) < valArr.get(j+1)) {
                    int temp = valArr.get(j+1);
                    valArr.set(j+1, valArr.get(j));
                    valArr.set(j, temp);
                }
            }
        }

        int temp = 0;
        int res = 0;
        for (int i = 0; i < valArr.size(); i ++) {
            if(temp < c) {
                temp += valArr.get(i);
                res += 1;
            } else {
                return res;
            }
        }
        return res;
        
    }
    
    
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int t: tangerine) {
            
            if(map.get(t) != null) {
                map.put(t, map.get(t) + 1);
                
            } else {
                map.put(t, 1);
            }
        }
        
        List<Integer> val = new ArrayList<>(map.values());      
        Collections.sort(val, Collections.reverseOrder());
        
        int temp = 0;
        int answer = 0;
        
        for (int v: val){
            if (temp < k) {
                temp += v;
                answer += 1;
            } else{
                return answer;
            }
        }
        return answer;
    }
}