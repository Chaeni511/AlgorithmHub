import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());


        int[][] knapsack = new int[N+1][K+1];

        int[][] stuff = new int[N+1][2];
        stuff[0][0] = 0;
        stuff[0][1] = 0;

        for(int i = 1; i < N+1; i++){
            st = new StringTokenizer(br.readLine());

            stuff[i][0] = Integer.parseInt(st.nextToken());
            stuff[i][1] = Integer.parseInt(st.nextToken());
            // System.out.println(Arrays.toString(stuff[i]));
        }

        for(int n = 1; n < N+1; n++){
            for(int k = 1; k<K+1; k++){
                int w = stuff[n][0];
                int v = stuff[n][1];

                if(k < w){
                    knapsack[n][k] = knapsack[n-1][k];
                } else {
                    knapsack[n][k] = Math.max(v+knapsack[n-1][k-w], knapsack[n-1][k]);
                }
            }
        }

        System.out.println(knapsack[N][K]);
       
    }
}
