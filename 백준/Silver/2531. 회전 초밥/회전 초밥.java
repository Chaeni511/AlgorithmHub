import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int d;
    static int k;
    static int c;
    static List<Integer> sushi;
   

    public static int sushi() {
        int e = k;
        int minLen = Math.min(d, k+1);
        
        HashMap<Integer, Integer> map = new HashMap<>();

        // 처음 초밥 k개 추가
        for(int i=0; i < k; i++){
            int initialSushi = sushi.get(i);

            if(map.get(initialSushi) == null) {

                map.put(initialSushi, 1);

            } else {

                map.put(initialSushi, map.get(initialSushi) + 1);
            }
        }
        
        // 쿠폰 초밥 추가
        if(map.get(c) == null){
            map.put(c, 1);
        } else {
            map.put(c, map.get(c)+1);
        }

        // max값 초기 설정
        int res = map.size();


        for(int s=0; s<n; s++) {

            int startSushi = sushi.get(s);
            int endSushi = sushi.get(e);

            // 맨 앞의 초밥 빼기
            if(map.get(startSushi) == 1){

                map.remove(startSushi);

            } else {

                map.put(startSushi, map.get(startSushi) - 1);
            }

            // 맨 뒤에 초밥 추가
            if(map.get(endSushi) == null){

                map.put(endSushi, 1);

            } else {

                map.put(endSushi, map.get(endSushi) + 1);

            }

            // max값 확인 및 업뎃
            res = Math.max(res, map.size());


            try {
                e = (e + 1) % n;
            } catch(Exception exc) {
                e = 0;
            }

            
            if (res >= minLen) {
                
                return res;
            }
        }
        
        return res;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);

        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        sushi = new ArrayList<Integer>(n);


        for(int i = 0; i < n; i++) {
            int s = Integer.parseInt(br.readLine());
            sushi.add(s);
        };

        System.out.println(sushi());
    }
}
