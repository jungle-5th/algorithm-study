// https://www.acmicpc.net/problem/17128
// 소가 정보섬에 올라온 이유

// 문제
// 소 N마리가 정보섬에 올라왔다!
// 소들은 정보섬 1층 앞마당에서 A_1, A_2, A_3, ..., A_N, A_1의 순서대로 동그랗게 앉아 쉬고 있다.
// 각 소들에게는 품질 점수 A_i가 적힌 스티커가 붙어 있다. 욱제는 소 떼 옆에서 효빈이가 계산해 둔 어떤 계산 식을 발견했는데, 그것은 아래와 같다.

// S = sum_{i=1}^N(A_{i}×A_{i+1}×A_{i+2}×A_{i+3}) (단, A_{N+1}=A_{1}, A_{N+2}=A_{2}, A_{N+3}=A_{3})

// 풀어 쓰자면, 원형으로 둘러 앉은 소들에 대해서, 연속한 네 마리 소들의 품질 점수를 곱한 값을 모두 더한 것이다.
// 욱제는 효빈이가 학교를 떠나지 못하도록 심술부릴 작정이다. 욱제는 총 Q번에 걸쳐 어떤 i번째 소를 선택할 것이다.
// 그러고는 A_i가 적힌 스티커를 떼어내고, -A_i이 적힌 스티커를 붙일 작정이다.
// 그러면 효빈이는 Q번에 걸쳐서 S를 다시 계산해야 한다. 한 번 바꾼 스티커는 다음에 또 다시 바꾸지 않는 이상 계속 유지된다.
// 효빈이의 절친인 당신은 악동 욱제에게 괴롭힘 받는 효빈이를 도와 주기로 했다. 효빈이를 도와 S를 계산해 보자!

// 입력
// 첫째 줄에 소의 수를 나타내는 N과 욱제가 장난칠 횟수 Q가 주어진다.

// 둘째 줄에 N마리 소들의 품질 점수 A_i가 순서대로 주어진다.셋째 줄에 욱제가 장난칠 Q개의 소의 번호 Q_i가 순서대로 주어진다.

// 출력
// Q개의 줄에 걸쳐 다시 계산된 S의 값을 출력한다.

// 제한
// 4 ≤ N ≤ 200000
// 1 ≤ Q ≤ 200000
// 1 ≤ |A_i| ≤ 10
// 1 ≤ Q_i ≤ N

// 예제 입력 1 
// 8 5
// -2 3 5 -6 10 -8 7 6
// 3 5 2 7 7

// 예제 출력 1 
// -1080
// 1920
// 4224
// 2376
// 4224

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;
import java.util.*;

public class Q17128 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    public static void main(String[] args) throws IOException {
        StringTokenizer firstInput = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(firstInput.nextToken());
        int q = Integer.parseInt(firstInput.nextToken());

        StringTokenizer cowsInput = new StringTokenizer(br.readLine());
        int[] cows = new int[n+3];
        for (int i = 0; i < n; i++) {
            cows[i] = Integer.parseInt(cowsInput.nextToken());
        }
        cows[n] = cows[0];
        cows[n+1] = cows[1];
        cows[n+2] = cows[2];
        int[] s = new int[n];
        BigInteger sum = BigInteger.valueOf(0); 
        
        for (int i = 0; i < n; i++) {
            int mul = cows[i]*cows[i+1]*cows[i+2]*cows[i+3];
            s[i] = mul;
            sum = sum.add(BigInteger.valueOf(mul));
        }

        StringTokenizer tricksInput = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int trick = Integer.parseInt(tricksInput.nextToken()) -1;
            int changed = 0;
            for (int j = 0; j < 4; j++) {
                int idx = trick-j;
                if (idx < 0) idx = n+idx;
                s[idx] = -s[idx];
                changed += 2*s[idx];
            }
            sum = sum.add(BigInteger.valueOf(changed));
            bw.write(sum.toString()+"\n");
        }
        bw.flush();
    }
}
