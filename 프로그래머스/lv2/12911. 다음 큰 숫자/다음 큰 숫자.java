class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int target = cnt(n);
        
        while (true) {
            n++;
            if (cnt(n) == target) {
                return n;
            }
        }
        // return answer;
    }
    
    public int cnt(int num) {
        int one = 0;

        String bin = Integer.toBinaryString(num);
        
        for (int i = 0; i < bin.length(); i++) {
            if (bin.charAt(i) == '1') {
                one++;
            }    
        }
        
        return one;
    }
}