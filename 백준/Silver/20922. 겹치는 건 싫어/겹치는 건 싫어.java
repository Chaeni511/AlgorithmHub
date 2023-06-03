import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        StringTokenizer nums = new StringTokenizer(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(nums.nextToken());
        }

        int res = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int s = 0;
        int temp = 0;

        for(int i = 0; i < n; i++) {
            if (!map.containsKey(arr[i])) {
                map.put(arr[i], 1);
                temp += 1;
            } else {
                if(map.get(arr[i]) < k) {
                    map.put(arr[i], map.get(arr[i]) + 1);
                    temp += 1;
                } else {
                    if (map.get(arr[i]) >= k) {
                        res = Math.max(res, temp);

                        while (map.get(arr[i]) == k) {
                            map.put(arr[s], map.get(arr[s]) - 1);
                            temp -= 1;
                            s += 1;
                        }
                    }

                    map.put(arr[s-1], map.get(arr[s-1]) + 1);
                    temp += 1;
                }
            }
        }

        res = Math.max(res, temp);

        System.out.println(res);
    }
}
