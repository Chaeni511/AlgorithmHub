class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        
        int cnr = (brown + 4)/2;
        int start = (brown + 4)/2;
        
        if (((brown + 4)/2) % 2 == 1) {
            start += 1;
        };
        
        for (int i = start/2; i <= cnr; i++) {
            
            int j = cnr - i;
            
            if ((i-2) * (j-2) == yellow) {
                
                answer[0] = i;
                answer[1] = j;
                
                break;
            }
        }
        
        return answer;
    }
}