import java.util.*;

class Solution {
    public int solution(int[] common) {
        
        int d = common[1] - common[0];
        if (common[1] + d == common[2]) {
            return common[common.length - 1] + d;
        } else {
            d = common[1] / common[0];
            return common[common.length - 1] * d;
        }
    }
}