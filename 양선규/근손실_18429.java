import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 근손실_18429 {
    
    // 결과 저장할 변수
    static int cnt = 0;

    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // N, K 입력받기
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 운동키트 입력받기
        st = new StringTokenizer(br.readLine());
        int kit[] = new int[N];
        for(int i = 0; i < N; i++) {
            kit[i] = Integer.parseInt(st.nextToken()) - K;
        }

        // 방문체크 배열
        boolean visited[] = new boolean[N];

        // 탐색 진행
        backTraking(0, 0, N, visited, kit);

        // 결과 출력
        System.out.println(cnt);

        
        br.close();
    }

    public static void backTraking(int depth, int sum, int N, boolean visited[], int kit[]) {
        
        // 최대 깊이에 도달했을 경우 cnt + 1 후 리턴
        if(depth == N) {
            cnt += 1;
            return;
        }

        // 방문 안했고 500이상이면 탐색 진행
        for(int i = 0; i < N; i++) {
            if(visited[i] == false && sum + kit[i] >= 0) {
                visited[i] = true;
                backTraking(depth + 1, sum + kit[i], N, visited, kit);
                visited[i] = false;
            }
        }
    }
}