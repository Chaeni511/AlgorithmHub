import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        Pair[] cars = new Pair[routes.length];
        
        for (int i = 0; i < routes.length; i++) {
            Pair pair = new Pair(routes[i][0], routes[i][1]);
            cars[i] = pair;
        }

        Arrays.sort(cars, (x, y) -> {
            return Integer.compare(x.end, y.end);
        });
      
        boolean[] visited = new boolean[routes.length];
        
        for (int i = 0; i < routes.length; i++) {
            
            if (!visited[i]) {
                
                visited[i] = true;
                
                for(int j = i; j < routes.length - 1; j++) {
                    if (cars[i].end >= cars[j+1].start) {
                        visited[j+1] = true;
                    }
                }
                
                answer++;
            }
        }
        
        return answer;
        
    }
    
    public class Pair {
        int start, end;
        Pair(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
}