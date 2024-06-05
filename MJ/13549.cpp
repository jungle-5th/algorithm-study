// https://www.acmicpc.net/problem/13549
// 숨바꼭질 3

// 문제
// 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
// 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
// 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
// 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

// 입력
// 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

// 출력
// 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

// 예제 입력 1 
// 5 17
// 예제 출력 1 
// 2

#include <iostream>

using namespace std;

int count[2] = {0,0};

void countones(int remainder, int pow, int idx) {

    int mox, rem;
    mox = remainder/(1<<pow);
    rem = remainder%(1<<pow);
    if(pow == 0) {
        count[idx] += mox;
        return;
    }
    if (((1<<pow) - rem) < (rem % (1<<pow-1))) {
        rem = (1<<pow) - rem;
        mox += 1;
    }
    count[idx] += mox;
    pow -= 1;
    countones(rem, pow, idx);
}


int main() {
/////////////////////////////////
int n, m;
cin >> n >> m;
if (m < n) {
    cout << n-m << endl;
    return 0;
}

if (n == m) {
    cout << 0 << endl;
    return 0;
}
int n_was_zero = 0;
if (n == 0) {
    n = 1;
    n_was_zero = 1;
}

int small, large;
for (int i = 0; i < 1000; i++) {
    int bipow = 1 << i;
    if(n*bipow == m) {
        cout << n_was_zero << endl;
        return 0;
    }
    if(n * bipow > m) {
        large = i;
        break;
    }
}
small = large-1;
int remainder;
countones(m-n*(1<<small), small, 0);
countones(n*(1<<large)-m, large, 1);

if (count[0] > count[1]) cout << count[1] + n_was_zero;
else cout << count[0] + n_was_zero;

/////////////////////////////////
return 0;}