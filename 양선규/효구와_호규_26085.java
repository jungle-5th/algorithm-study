import java.io.*;
import java.util.*;

public class 효구와_호규_26085 {
    public static void main(String[] args) throws Exception {
        
        // 무한 값 표현
        int INF = Integer.MAX_VALUE;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // N, M 입력받기
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 요소 총 갯수
        int count = N * M;

        // 0갯수, 1갯수
        int zeroCount = 0;
        int oneCount = 0;

        // board 입력받기
        int board[][] = new int[N][M];
        for(int x = 0; x < N; x++) {
            st = new StringTokenizer(br.readLine());
            for(int y = 0; y < M; y ++) {

                // 입력받으며 0 갯수를 센다
                board[x][y] = Integer.parseInt(st.nextToken());
                if(board[x][y] == 1) {
                    zeroCount += 1;
                }
            }
        }
        // 1 갯수는 총 갯수 - 0 갯수이다
        oneCount = count - zeroCount;

        System.out.println(killCard(count, zeroCount, oneCount, N, M, board, INF));
    }
    
    public static boolean deleteGo(int nx, int ny, int cx, int cy, int[][] board, int N, int M, int INF){
        
        // 다음 좌표가 안에 있고 / 현재카드가 INF 아니고 /  현재 카드와 다음 좌표 숫자가 같으면 지우기
        if(0 <= nx && nx < N && 0 <= ny && ny < M && board[cx][cy] != INF && board[nx][ny] == board[cx][cy]) {
            board[cx][cy] = INF;
            board[nx][ny] = INF;

            // 지웠으면 true 리턴
            return true;
        }
        // 못지웠으면 false 리턴
        return false;
    }

    public static int killCard(int count, int zeroCount, int oneCount, int N, int M, int[][] board, int INF) {

        // 상하좌우 이동 좌표
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        int nx;
        int ny;
        boolean result;

        // 총 갯수가 홀수일 경우 ( 0, 1 둘 중 하나는 무조건 홀수다 )
        if(count % 2 == 1) {
            return -1;
        }

        // 0 또는 1이 홀수일 경우 ( 총 갯수가 짝수여도 둘 중 하나가 홀수일 수 있음)
        if(zeroCount % 2 == 1 || oneCount % 2 == 1) {
            return -1;
        }

        // 모든 좌표에 대하여 상하좌우에 같은 값이 있는지 검사
        // 배열에 빈 공간이 2개라면, 배열의 크기가 몇이든 모든 값이 섞일 수 있다.
        // 즉 한 번이라도 삭제가 되었다면, 모든 값을 삭제할 수 있다
        for(int x = 0; x < N; x++) {
            for(int y = 0; y < M; y++) {
                for(int i = 0; i < 4; i++) {
                    nx = x + dx[i];
                    ny = y + dy[i];
                    result = deleteGo(nx, ny, x, y, board, N, M, INF);

                    // 한 번이라도 True라면(삭제되었다면)
                    if(result) {
                        return 1;
                    }
                } 
            }
        }
        return -1;
    }
}
