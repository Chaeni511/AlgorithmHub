import java.util.*;

class Solution {
    static int[] answer = {0, 0, 0, 0};
    static int[] forward = new int[1000000];
    static int[] backward = new int[1000000];
    static int nodeCnt = 0;

    public int[] solution(int[][] edges) {
        
        // edges를 map으로 만들기 
        for(int[] edge: edges) {
            int from = edge[0];
            int to = edge[1];
            
            // 노드수 확인
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
            if (out == 0) {
                answer[2]++;
            } else if (out == 2) {
                int in = backward[i];
                if (in > 0) {
                    answer[3]++;
                } else {
                    answer[0] = i;
                }
            } else if (out > 2) {
                answer[0] = i;
            }       
        }
        answer[1] = forward[answer[0]] - answer[2] - answer[3];
        
        return answer;
    }
    
//     public void dfs(int n1) {
//         if (visited[n1]) {
//             return;
//         }
//         visited[n1] = 1;

//         List<Integer> neighbors = map.get(n1);
//         for(int n2: neighbors) {
//             visited[n2] = 1;
//             dfs(n2);
//         }
        
//     }
}

// // 막대 그래프 마지막 노드
// if (neighbors == null){
//     answer[2]++;
//     return;
// }

// // 도넛 그래프
// if (visited[n1] == 1 && neighbors.size() == 1) {
//     answer[1]++;
//     return;
// }

// // 8자 그래프 교차점
// if (neighbors.size() == 2) {
//     answer[3]++;
//     return;
// }