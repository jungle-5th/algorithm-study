import java.util.*;
import java.io.*;


public class _4781 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // n: 가게에 있는 사탕 종류의 수
        // m: 가지고 있는 돈
        int n = Integer.parseInt(st.nextToken());
        int m = (int)(Double.parseDouble(st.nextToken())*100+0.5);

        // 돈의 양이 소수점 둘째자리까지 주어지는데 어떻게 처리하지?
        // 그냥 100 곱해서 정수로 만들어버리자.

        while(n!=0 || m!=0){
            int[] dp = new int[m + 1];
            for(int i = 0; i < n; i++){
                st = new StringTokenizer(br.readLine());
                // c: 칼로리
                // p: 가격
                int c = Integer.parseInt(st.nextToken());
                int p = (int)(Double.parseDouble(st.nextToken())*100+0.5);
                // dp[j]: j원으로 얻을 수 있는 최대 칼로리

                // p<=j<=m까지 탐색하며 j값일 때 최대 칼로리를 갱신
                for(int j = p; j <= m; j++){
                    dp[j] = Math.max(dp[j], dp[j - p] + c);
                }
            }
            System.out.println(dp[m]);

            // 다음 입력을 받기
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = (int)(Double.parseDouble(st.nextToken()) * 100+0.5);
        }
    }
}