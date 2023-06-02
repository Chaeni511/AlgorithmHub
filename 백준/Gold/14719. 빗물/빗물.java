import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        int[] blocks = new int[w];

        StringTokenizer b = new StringTokenizer(br.readLine());

        for (int i = 0; i < w; i++){
            blocks[i] = Integer.parseInt(b.nextToken());
        }

        int res = 0;

        for(int i = 1; i < w-1; i++) {
            int left = 0;
            int right = 0;

            for(int j = 0; j<i; j++){
                left = Math.max(left, blocks[j]);
            }

            for(int j = i+1; j <w; j++){
                right = Math.max(right, blocks[j]);
            }
            
            int bottom = Math.min(left, right);

            if (blocks[i] < bottom) {
                res += bottom - blocks[i];
            }
        }

        System.out.println(res);
    }
    
}
