import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Comparator;
import java.util.Arrays;

public class 내일_할거야_7983 {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // N 입력받기
        int N = Integer.parseInt(br.readLine());

        // 소요일, 마감일 입력받기
        int DT[][] = new int[N][2];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for(int j = 0; j < 2; j++) {
                DT[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 마감일 기준 내림차순 정렬
        Arrays.sort(DT, Comparator.comparingInt((int[] a) -> a[1]).reversed());

        // 쉴 수 있는 시간을 계산할 변수
        // 초기값은 과제 중 가장 긴 마감일
        int day = DT[0][1];

        // 소요일, 마감일 저장할 변수
        int s;
        int e;

        // day와 마감일 중 작은 시간에서 소요일을 뺀다.
        // 둘 중 더 큰 값은 의미가 없어지기 때문
        // day가 길어도 마감일이 짧으면 마감일에 맞춰야 한다.
        // 과제의 마감일이 길어도 정작 남은 day가 짧으면 day에 맞춰야 한다. ( 앞서 계산된 특정 과제가 오랜 기간이 걸렸을 경우 이럴 수 있다 )
        for(int i = 0; i < N; i++) {

            // 현재 과제의 소요일, 마감일
            s = DT[i][0];
            e = DT[i][1];

            // day와 e 중 작은 값에서 소요일을 빼 준다
            day = Math.min(day, e) - s;
        }

        // 결과 출력
        System.out.println(day);

        br.close();
    }
}