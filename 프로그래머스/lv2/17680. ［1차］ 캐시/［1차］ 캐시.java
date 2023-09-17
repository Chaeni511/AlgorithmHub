import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        if (cacheSize == 0) {
            return 5 * cities.length;
        }
        
        List<String> cache = new ArrayList<>();

        LinkedList<String> frequency = new LinkedList<>();  

        for (String cc : cities) {
            String city = cc.toLowerCase();

            if (cache.size() < cacheSize) {
                if(cache.contains(city)){
                    answer++;
                } else {
                    cache.add(city);
                    answer += 5;
                }

            } else {

                if (cache.contains(city)) {
                    answer++;

                } else {
                    answer += 5;

                    int maxFrequency = -1;
                    String maxFrequencyCity = "";

                    for (String c: cache) {
                        if (frequency.indexOf(c) > maxFrequency) {
                            maxFrequency = frequency.indexOf(c);
                            maxFrequencyCity = c;
                        }
                    }

                    cache.remove(maxFrequencyCity);
                    cache.add(city);
                }
            }
            frequency.addFirst(city);

        }
    
        
        return answer;
    }
}