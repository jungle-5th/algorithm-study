import java.io.*;
import java.util.*;

public class 특별상이라도_받고_싶어_24460 {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // x, y의 길이
        int N = Integer.parseInt(br.readLine());

        // 좌석별 추첨번호 입력받기
        int board[][] = new int[N][N];
        StringTokenizer st;
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(special(0, 0, N, board));
    }


    // 시작 좌표, 변의 길이, 좌석별 추첨번호 입력받기
    public static int special(int x, int y, int N, int[][] board) {
        
        // 사람이 1명이면 그 사람을 뽑는다
        if(N == 1) {
            return board[0][0];
        }

        // 사람이 4명이면 번호가 2번째로 작은 사람 고르기
        if(N == 2) {
            int arr[] = new int[4];
            int index = 0;
            for(int i = x; i < x + N; i++) {
                for(int j = y; j < y + N; j++) {
                    // 배열에 4개의 추첨번호를 저장
                    arr[index++] = board[i][j];
                }
            }
            // 정렬 후 2번째로 작은 값 리턴
            Arrays.sort(arr);
            return arr[1];
        }

        // 사람이 4명보다 많다면 4등분으로 나누어 추첨번호 고르기
        else {
            int arr[] = new int[4];
            arr[0] = special(x, y, N/2, board);
            arr[1] = special(x, y + N/2, N/2, board);
            arr[2] = special(x + N/2, y, N/2, board);
            arr[3] = special(x + N/2, y + N/2, N/2, board);

            // 고른 번호 중 2번째로 작은 값 리턴
            Arrays.sort(arr);
            return arr[1];
        }
    }
}