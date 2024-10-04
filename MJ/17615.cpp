// https://www.acmicpc.net/problem/17615
// 볼 모으기

// 문제
// 빨간색 볼과 파란색 볼이 <그림 1>에서 보인 것처럼 일직선상에 섞여 놓여 있을 때, 볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다.
// 볼을 옮기는 규칙은 다음과 같다.
// 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다.
// 즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
// 유사하게, 파란색 볼은 옆에 있는 빨간색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
// 옮길 수 있는 볼의 색깔은 한 가지이다. 즉, 빨간색 볼을 처음에 옮겼으면 다음에도 빨간색 볼만 옮길 수 있다.
// 유사하게, 파란색 볼을 처음에 옮겼으면 다음에도 파란색 볼만 옮길 수 있다.

// 입력
// 첫 번째 줄에는 볼의 총 개수 N이 주어진다. (1 ≤ N ≤ 500,000)
// 다음 줄에는 볼의 색깔을 나타내는 문자 R(빨간색 볼) 또는 B(파란색 볼)가 공백 없이 주어진다.
// 문자열에는 R 또는 B 중 한 종류만 주어질 수도 있으며, 이 경우 답은 0이 된다.

// 출력
// 최소 이동횟수를 출력한다.

// 예제 입력 1 
// 9
// RBBBRBRRR
// 예제 출력 1 
// 2
// 예제 입력 2 
// 8
// BBRBBBBR
// 예제 출력 2 
// 1

#include <iostream>
using namespace std;

int minval = 1000000000;
void ballball(string str) {
    int count = 0, red = 100000000, blue = 1000000000;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] == 'R') {
            red = i;
            if (blue < i) {
                red = blue;
                blue = i;
                count++;
                if (count == minval) break;
            }
        }
        else blue = i;
    }
    minval = count;
    count = 0, red = 1000000000, blue = 1000000000;
        for (int i = 0; i < str.size(); i++) {
        if (str[i] == 'B') {
            blue = i;
            if (red < i) {
                blue = red;
                red = i;
                count++;
                if (count == minval) break;
            }
        }
        else red = i;
    }
    minval = count;
    count = 0, red = -1, blue = -1;
    for (int i = str.size()-1; i >= 0; i--) {
        if (str[i] == 'R') {
            red = i;
            if (blue > i) {
                red = blue;
                blue = i;
                count++;
                if (count == minval) break;
            }
        }
        else blue = i;
    }
    minval = count;
    count = 0, red = -1, blue = -1;
        for (int i = str.size()-1; i >= 0; i--) {
        if (str[i] == 'B') {
            blue = i;
            if (red > i) {
                blue = red;
                red = i;
                count++;
                if (count == minval) break;
            }
        }
        else red = i;
    }
    minval = count;
}

int main() {
/////////////////////////////////////////////
int length; cin >> length;
string str; cin >> str;
ballball(str);
cout << minval;
/////////////////////////////////////////////
return 0;}