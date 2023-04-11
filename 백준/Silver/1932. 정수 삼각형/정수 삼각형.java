import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/**
 * Main_1932
 */
public class Main {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 5
        // 7
        // 3 8
        // 8 1 0
        // 2 7 4 4
        // 4 5 2 6 5
        
        int n = Integer.parseInt(br.readLine());

        ArrayList<Integer>[] arr = new ArrayList[n];
        ArrayList<Integer>[] dp = new ArrayList[n];

        // 입력을 정말 이따구로 밖에 받을 수 없는 것인가...?
        for(int i = 0; i < n; i++) {
            // 입력 스트림은 하나만 받아서 쓰면 됩니다.
            // BufferedReader br_triangle = new BufferedReader(new InputStreamReader(System.in));
            String line = br.readLine();
            StringTokenizer st = new StringTokenizer(line);
            int cnt = st.countTokens();

            arr[i] = new ArrayList<Integer>();
            dp[i] = new ArrayList<Integer>();

            for(int j = 0; j < cnt; j++){
                arr[i].add(Integer.parseInt(st.nextToken()));
                dp[i].add(0);
            }
        }

        dp[0].set(0, arr[0].get(0));

        for(int i = 0; i < n; i++){

            int arr_len = dp[i].size();

            for(int j = 0; j < arr_len; j++) {

                if(i+1 < n){

                    dp[i+1].set(j, Math.max(Math.max(arr[i+1].get(j) + dp[i].get(j), arr[i+1].get(j)), dp[i+1].get(j)));
                    dp[i+1].set(j+1, Math.max(Math.max(arr[i+1].get(j+1) + dp[i].get(j), arr[i+1].get(j+1)), dp[i+1].get(j+1)));

                }
            }
        }

        System.out.println(Collections.max(dp[n-1]));

    }
}