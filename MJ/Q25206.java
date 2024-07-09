// https://www.acmicpc.net/problem/25206
// 너의 평점은

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


public class Q25206 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception {
        int totalTime = 0;
        double totalGrade = 0;
        Map<String, Double> dict = new HashMap<>(){{
            put("A+", 4.5);
            put("A0" , 4.0);
            put("B+", 3.5);
            put("B0", 3.0);
            put("C+", 2.5);
            put("C0", 2.0);
            put("D+", 1.5);
            put("D0", 1.0);
            put("F", 0.0);
        }};

        for (int i = 0; i < 20; i++) {
            StringTokenizer input = new StringTokenizer(br.readLine());
            String gwa = input.nextToken();
            Double time = Double.parseDouble(input.nextToken());
            String grade = input.nextToken();
            if (grade.equals("P")) continue;
            else {totalTime += time; totalGrade += dict.get(grade)*time;}
        }
        System.out.println(totalGrade/totalTime);
    }
}
