import java.io.*;
import java.util.*;

public class 보물_1026 {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // N 입력받기
        int N = Integer.parseInt(br.readLine());

        // a, b 배열 생성
        int a[] = new int[N];
        int b[] = new int[N];
        
        // a 배열 입력받기
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        // a 배열 내림차순 정렬
        Arrays.sort(a);
        for(int i = 0; i < a.length / 2; i++) {
            int temp = a[i];
            a[i] = a[a.length - 1 - i];
            a[a.length - 1 - i] = temp;
        }

        // b 배열 입력받기
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        // 결과값을 저장할 변수
        int result = 0;

        // a의 가장 큰 값과 b의 가장 작은 값을 곱하여 result에 더해준다
        for(int i = 0; i < N; i++) {
            int minIndex = findMinIndex(b);
            result += a[i] * b[minIndex];
            b[minIndex] = Integer.MAX_VALUE;
        }

        System.out.println(result);
    }

    // 배열에서 가장 작은 값의 인덱스를 찾는 함수
    public static int findMinIndex(int[] arr) {
        int minIndex = 0;
        for(int i = 1; i < arr.length; i++) {
            if(arr[i] < arr[minIndex]) {
                minIndex = i;
            }
        }
        return minIndex;
    }
}