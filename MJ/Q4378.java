// https://www.acmicpc.net/problem/4378
// 트ㅏㅊ;

// 문제
// 가끔, 그러나 때때로, 우리들은 키보드에서 양손을 오른쪽으로 한 칸씩 이동한 상태로 두고 타자를 치는 경우가 있다.
// 즉, "ACMICPC.NET"을 위와 같은 방법으로 치게 되면 "SV,OV[V/MRY"이라는 이상한 문장을 보게 된다.
// 교준이는 장문을 쓰는데, 너무 급한 나머지 위와 같은 오류를 범한 채로 글을 완성해 버렸다. 이 글을 다시 쓰는 것은 교준이에게는 너무 힘든 일이다.
// 교준이를 대신해서 오류를 고쳐주자.

// 입력
// 입력은 여러 줄로 이루어진다. 각 줄은 숫자나 공백, 알파벳 대문자, 위의 키보드에 표시되어 있는 문장 부호로 이루어져 있다.
// Q, A, Z나 `(back-quote), 단어로 이루어진 키(Tab, BackSp, Control 등)는 입력의 각 줄에 포함되지 않는다.
// 예외적으로 공백(' ', SpaceBar)은 입력으로 들어올 수 있는데, 스페이스 바는 너무 길어서 교준이가 위의 오류를 범하지 않는다.

// 출력
// 각 줄마다 오류를 고쳐 출력한다.

// 예제 입력 1 
// O S, GOMR YPFSU/
// 예제 출력 1 
// I AM FINE TODAY.

import java.util.*;

public class Q4378 {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        while (sc.hasNextLine()){
        String input = sc.nextLine();
        int i = 0;
        String res = "";
        while (i < input.length()) {
            char c = input.charAt(i);
            char d = ' ';
            switch (c) {
                case '1':
                    d = '`';
                    break;
                case '2':
                    d = '1';
                    break;
                case '3':
                    d = '2';
                    break;
                case '4':
                    d = '3';
                    break;
                case '5':
                    d = '4';
                    break;
                case '6':
                    d = '5';
                    break;
                case '7':
                    d = '6';
                    break;
                case '8':
                    d = '7';
                    break;
                case '9':
                    d = '8';
                    break;
                case '0':
                    d = '9';
                    break;
                case '-':
                    d = '0';
                    break;
                case '=':
                    d = '-';
                    break;

                case 'W':
                    d = 'Q';
                    break;
                case 'E':
                    d = 'W';
                    break;
                case 'R':
                    d = 'E';
                    break;
                case 'T':
                    d = 'R';
                    break;
                case 'Y':
                    d = 'T';
                    break;
                case 'U':
                    d = 'Y';
                    break;
                case 'I':
                    d = 'U';
                    break;
                case 'O':
                    d = 'I';
                    break;
                case 'P':
                    d = 'O';
                    break;
                case '[':
                    d = 'P';
                    break;
                case ']':
                    d = '[';
                    break;
                case '\\':
                    d = ']';
                    break;

                case 'S':
                    d = 'A';
                    break;
                case 'D':
                    d = 'S';
                    break;
                case 'F':
                    d = 'D';
                    break;
                case 'G':
                    d = 'F';
                    break;
                case 'H':
                    d = 'G';
                    break;
                case 'J':
                    d = 'H';
                    break;
                case 'K':
                    d = 'J';
                    break;
                case 'L':
                    d = 'K';
                    break;
                case ';':
                    d = 'L';
                    break;
                case '\'':
                    d = ';';
                    break;

                case 'X':
                    d = 'Z';
                    break;
                case 'C':
                    d = 'X';
                    break;
                case 'V':
                    d = 'C';
                    break;
                case 'B':
                    d = 'V';
                    break;
                case 'N':
                    d = 'B';
                    break;
                case 'M':
                    d = 'N';
                    break;
                case ',':
                    d = 'M';
                    break;
                case '.':
                    d = ',';
                    break;
                case '/':
                    d = '.';
                    break;
                case ' ':
                    d = ' ';
                    break;               
                default:
                    break;
            }
            res += d;
            i++;
        }
        System.out.println(res);
    }}
}