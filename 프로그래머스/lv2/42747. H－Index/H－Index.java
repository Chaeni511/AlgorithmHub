class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        int h = 0;
        for (int citation: citations) {
            if (citation > h) {
                h = citation;
            }
        }
        
        while (h > 0) {
            int cnt = 0;
            Boolean flag = true;
            
            for (int citation : citations) {
                // if (cnt > h) {
                //     flag = false;
                //     break;
                // }
                if (citation >= h) {
                    cnt += 1;
                }
            }
            
            if (cnt >= h) {
                return h;
            }
            // if (flag && cnt == h) {
            //     return h;
            // }
            
            h--;
        }
        return h;
    }
}