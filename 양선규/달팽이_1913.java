import java.io.*;

public class 달팽이_1913 {
    public static void main(String[] args) throws Exception {
        
        StringBuilder sb = new StringBuilder();
        
        // 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());

        // 2차원 배열 생성
        int board[][] = new int[N][N];
        int resultX = Integer.MIN_VALUE;
        int resultY = Integer.MIN_VALUE;

        // 시작 좌표
        int x = N / 2;
        int y = N / 2;

        // 첫 숫자는 먼저 입력해 둔다
        board[x][y] = 1;
        int num = 2;
        for(int i = 1; i < N; i++) {

            // i가 홀수일 때, x는 줄어들고 y는 늘어난다
            if(i % 2 == 1) {
                for(int j = 1; j < i+1; j++) {
                    x -= 1;
                    board[x][y] = num;
                    num += 1;
                }
                for(int j = 1; j < i+1; j++) {
                    y += 1;
                    board[x][y] = num;
                    num += 1;
                }
            }

            // i가 짝수일 때, x는 늘어나고 y는 줄어든다
            else {
                for(int j = 1; j < i+1; j++) {
                    x += 1;
                    board[x][y] = num;
                    num += 1;
                }
                for(int j = 1; j < i+1; j++) {
                    y -= 1;
                    board[x][y] = num;
                    num += 1;
                }
            }

            // 마지막 반복엔 x를 한번 더 빼준다
            if(i == N - 1) {
                for(int j = 1; j < i+1; j++) {
                    x -= 1;
                    board[x][y] = num;
                    num += 1;
                }
            }
        }

        // 출력
        for(int i = 0; i < N; i ++) {
            for(int j = 0; j < N; j ++) {
                sb.append(board[i][j]).append(" ");
                if(board[i][j] == target) {
                    resultX = i + 1;
                    resultY = j + 1;
                }
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
        System.out.printf("%d %d", resultX, resultY);
    }
}