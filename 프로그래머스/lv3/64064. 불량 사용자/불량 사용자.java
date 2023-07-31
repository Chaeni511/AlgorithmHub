import java.util.*;

class Solution {
    // static int answer = 0;
    static List<Set> answer = new ArrayList();
    // static List<Array> answer = new ArrayList();
    
    public int solution(String[] user_id, String[] banned_id) {
    // public Map solution(String[] user_id, String[] banned_id) {
        Map<String, Set<String>> map = new HashMap<>();

        for (String ban : banned_id) {
            for (String user : user_id) {

                if (ban.length() == user.length() && check(user, ban)) {

                    Set<String> tmp;

                    if (map.containsKey(ban)) {
                        tmp = new HashSet<>(map.get(ban));
                    } else {
                        tmp = new HashSet<>();
                    }

                    tmp.add(user);
                    map.put(ban, tmp);
                }
            }
        }
        // return map;
        comb(0, banned_id, map, new HashSet<String>());
        return answer.size();
        // return banned_id.length;
    }

    private Boolean check(String user, String ban) {
        for (int i = 0; i < user.length(); i++) {
            if (ban.charAt(i) != '*' && ban.charAt(i) != user.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    private void comb(int idx, String[] keys, Map<String, Set<String>> map, Set<String> set) {
        if (idx == keys.length && !answer.contains(set)) {
            // answer += 1;
            Set<String> copy = new HashSet<>(set);

            answer.add(copy);            
        }

        if (idx == keys.length) {
            return;
        }

        for (String id : new HashSet<String>(map.get(keys[idx]))) {
            if (!set.contains(id)) {
                set.add(id);
                comb(idx + 1, keys, map, set);
                set.remove(id);
            }
        }
    }
}
