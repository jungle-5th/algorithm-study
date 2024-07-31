// https://www.acmicpc.net/problem/10974
// 모든 순열

// 문제
// N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

// 출력
// 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

// 예제 입력 1 
// 3
// 예제 출력 1 
// 1 2 3
// 1 3 2
// 2 1 3
// 2 3 1
// 3 1 2
// 3 2 1

import java.util.Scanner;
import java.util.ArrayList;
public class Q10974 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        ArrayList<Integer> set = new ArrayList<>();
        String str = "";
        for (int q = 1; q <= n; q++) {set.add(q);}
        permul(set, str);
        scanner.close();
    }

    static void permul(ArrayList<Integer> set, String str) {
        String newstr = str;
        if (set.size() == 1) {
            newstr = str + set.get(0);
            System.out.println(newstr);
            return;
        }

        for (int i = 0; i < set.size(); i++) {
            int num = set.get(i);
            newstr = str + num + " ";
            set.remove(i);
            permul(set, newstr);
            set.add(i, num);
        }
    }
}
