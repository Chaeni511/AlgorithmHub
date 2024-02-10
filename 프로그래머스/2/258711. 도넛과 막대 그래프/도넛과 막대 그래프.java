import java.util.*;

class Solution {
    static int[] answer = {0, 0, 0, 0};
    static int[] forward = new int[1000000];
    static int[] backward = new int[1000000];
    static int nodeCnt = 0;

    public int[] solution(int[][] edges) {
        
        // 각 edge에서 오고 갈 수 있는 노드수 저장 
        for(int[] edge: edges) {
            int from = edge[0];
            int to = edge[1];
            
            // 전체 노드수 확인
            if (from > nodeCnt) {
                nodeCnt = from;
            }
            if (to > nodeCnt) {
                nodeCnt = to;
            }
            
            // 정방향 저장
            forward[from]++;
            
            // 역방향 저장
            backward[to]++;   
        }
        
        
        for (int i = 1; i <= nodeCnt; i++) {
            int out = forward[i];
            // 갈 수 있는 곳이 없을 때
            // 막대 그래프
            if (out == 0) {
                answer[2]++;
                
            // 갈 수 있는 곳이 2개 일 때
            } else if (out == 2) {
                int in = backward[i];
                
                // 들어오는 노드가 있으면 8자 그래프
                if (in > 0) {
                    answer[3]++;
                    
                // 들어오는 노드가 없으면 시작 정점
                } else {
                    answer[0] = i;
                }
            // 갈 수 있는 노드가 2개 이상일 때
            // 시작 정점
            } else if (out > 2) {
                answer[0] = i;
            }       
        }
        
        // 도넛 그래프 개수
        answer[1] = forward[answer[0]] - answer[2] - answer[3];
        
        return answer;
    }
}