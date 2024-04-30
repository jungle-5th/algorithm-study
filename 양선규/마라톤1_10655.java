import java.io.*;
import java.util.*;

public class 마라톤1_10655 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 체크포인트 입력받기
        int N = Integer.parseInt(br.readLine());
        int cp[][] = new int[N][2];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            cp[i][0] = Integer.parseInt(st.nextToken());
            cp[i][1] = Integer.parseInt(st.nextToken());
        }

        int distance = 0;
        int diff = 0;
        int point;
        int point2;
        int point3;

        for(int i = 0; i < N - 1; i++) {

            point = Math.abs(cp[i][0] - cp[i+1][0]) + Math.abs(cp[i][1] - cp[i+1][1]);

            distance += point;

            if(i == N - 2) {
                break;
            }

            point2 = Math.abs(cp[i+1][0] - cp[i+2][0]) + Math.abs(cp[i+1][1] - cp[i+2][1]);
            point3 = Math.abs(cp[i][0] - cp[i+2][0]) + Math.abs(cp[i][1] - cp[i+2][1]);

            if(diff < Math.abs(point + point2) - point3) {
                diff = Math.abs(point + point2) - point3;
            }
        }
        distance -= diff;

        System.out.println(distance);
    }
}