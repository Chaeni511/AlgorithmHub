import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new LinkedList<Integer>();
        
        String[] tmpToday = today.split("[.]");
        int TODAY = Integer.parseInt(tmpToday[0]) * 12 * 28 + Integer.parseInt(tmpToday[1]) * 28 + Integer.parseInt(tmpToday[2]);
        
        Map<String, Integer> EXP = new HashMap<String, Integer>();
        for (String term: terms) {
            String[] tmp = term.split(" ");
            EXP.put(tmp[0], Integer.parseInt(tmp[1]) * 28);
        }
        
        for (int i = 0; i < privacies.length; i++) {
            String[] privacy = privacies[i].split(" ");
            
            String[] tmpExp = privacy[0].split("[.]");
            int exp = Integer.parseInt(tmpExp[0]) * 12 * 28 + Integer.parseInt(tmpExp[1]) * 28 + Integer.parseInt(tmpExp[2]);
            
            String term = privacy[1];
            
            if(exp + EXP.get(term) <= TODAY) {
                answer.add(i+1);
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}