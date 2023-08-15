import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        int af = 0;
        int ar = A.length - 1;
        int bf = 0;
        int br = B.length - 1;

        while (af <= ar) {
            if (A[af] * B[br] < B[bf] * A[ar]) {
                answer += A[af] * B[br];
                af++;
                br--;
            } else {
                answer += A[ar] * B[bf];
                ar--;
                bf++;
            }
        }

        return answer;
    }
}