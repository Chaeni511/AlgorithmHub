import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, Boolean> memo = new HashMap<String, Boolean>(n);

        for(int i=0; i<n; i++){

            memo.put(br.readLine(), true);
        }

        for(int i=0; i<m; i++) {

            StringTokenizer stk = new StringTokenizer(br.readLine(), ",");

            while(stk.hasMoreTokens()){

                String temp = stk.nextToken();

                if(memo.containsKey(temp)){

                    memo.remove(temp);
                    n -= 1;
                };
            }

            System.out.println(n);
        }
    }
}
