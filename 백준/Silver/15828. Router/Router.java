import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Deque<Integer> buffer = new ArrayDeque<>();

        while(true) {
            int packet = Integer.parseInt(br.readLine());
            if(packet == -1) {
                break;
            }
            if(packet == 0) {
                buffer.removeFirst();
            }else if(buffer.size() < N) {
                buffer.addLast(packet);
            }
        }

        StringBuilder sb = new StringBuilder();

        if(buffer.isEmpty()) {
            System.out.println("empty");
        }else {
            int bufferSize = buffer.size();
            for(int i = 0; i < bufferSize; i++) {
                sb.append(buffer.removeFirst()).append(" ");
            }
            System.out.println(sb.toString());
        }


    }
}
