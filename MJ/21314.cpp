// https://www.acmicpc.net/problem/21314
// 민겸 수

// 문제
// 민겸이는 로마 숫자를 보고 굉장히 흥미롭다고 생각했다. 그래서 민겸이는 새로운 수 체계인 민겸 수를 창조했다.
// 민겸 숫자는 0 이상의 정수 N에 대해 10^N 또는 5*10^N 꼴의 십진수를 대문자 M과 K로 이루어진 문자열로 표기한다.
// 10^N 꼴의 십진수는 N + 1개의 M으로, 5*10^N 꼴의 십진수는 N개의 M 뒤에 1개의 K를 이어붙인 문자열로 나타낸다.

// 즉, 아래 표처럼 나타낼 수 있다.
// 변환 전	변환 후
// 1	M
// 5	K
// 10	MM
// 50	MK
// 100	MMM
// 500	MMK
// 1000	MMMM
// 5000	MMMK
// ...	...
// 민겸 수는 한 개 이상의 민겸 숫자를 이어붙여 만든다. 예를 들어, 민겸 수 MKKMMK는 MK, K, MMK의 세 민겸 숫자를 이어붙여 만들 수 있다.
// 민겸 수를 십진수로 변환할 때는, 1개 이상의 민겸 숫자로 문자열을 분리한 뒤, 각각의 민겸 숫자를 십진수로 변환해서 순서대로 이어붙이면 된다.
// 민겸 숫자를 십진수로 변환하는 것은 십진수를 민겸 숫자로 변환하는 과정을 거꾸로 하면 된다.
// 예를 들어, 민겸 수 MKKMMK는 아래 그림과 같이 여러 가지 십진수로 변환할 수 있다.
// 민겸이는 위와 같이 하나의 민겸 수가 다양한 십진수로 변환될 수 있다는 사실을 알았다.
// 문득 민겸이는 변환될 수 있는 십진수 중 가장 큰 값과 가장 작은 값이 궁금해졌다.
// 민겸이를 위해 하나의 민겸 수가 십진수로 변환되었을 때 가질 수 있는 최댓값과 최솟값을 구해주자.

// 입력
// 민겸 수 하나가 주어진다. 민겸 수는 대문자 M과 K로만 이루어진 문자열이며, 길이는 3,000을 넘지 않는다.

// 출력
// 주어진 민겸 수가 십진수로 변환되었을 때 가질 수 있는 값 중 가장 큰 값과 가장 작은 값을 두 줄로 나누어 출력한다.

#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {

string minkyeom;
cin >> minkyeom;
string minmin, maxmin;
int mincount = 0;
string minimin;
string minimax;
for (size_t i = 0; i < minkyeom.length(); i++) {

    if (minkyeom[i] == 'M') {
        if (mincount != 0) {
            minimin += '0';
            minimax += '0';
        }
        mincount++;
    }
    else {
        if (mincount == 0) {
            maxmin += '5';
            minmin += '5';
            continue;
        }
        else {

        // minmin
        minimin = '1' + minimin;
        minimin += '5';
        minmin += minimin;
        minimin.clear();


        //maxmin
        minimax = '5' + minimax;
        minimax += '0';
        maxmin += minimax;
        minimax.clear();

        mincount = 0;
        }
    }
}

if (mincount != 0) {
    for (int i = 0; i < mincount; i++) maxmin += "1";
    minmin += "1";
    for (int i = 1; i < mincount; i++) minmin += "0";
}

cout << maxmin <<endl;
cout << minmin << endl;

}