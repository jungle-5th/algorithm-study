// https://www.acmicpc.net/problem/15918
// 랭퍼든 수열쟁이야!!

// 문제
// 랭퍼드 수열은 다음 조건을 만족하는 길이 2n의 수열이다.
// 1 이상 n 이하의 자연수가 각각 두 개씩 들어 있다.
// 두 개의 1 사이에는 정확히 1개의 수가 있다.
// 두 개의 2 사이에는 정확히 2개의 수가 있다.
// ...
// 두 개의 n 사이에는 정확히 n개의 수가 있다.
// 예를 들어 3, 1, 2, 1, 3, 2은 n=3인 랭퍼드 수열이다.
// n이 주어졌을 때, 길이 2n의 랭퍼드 수열의 개수를 구하면 된다.
// 하지만 이렇게만 하면 재미가 없으니 조건 하나를 추가하고자 한다. x번째 수와 y번째 수는 같다는 조건이다.
// (이 번호는 1부터 시작한다.)

// 입력
// 세 자연수 n, x, y가 주어진다. (2 ≤ n ≤ 12, 1 ≤ x < y ≤ 2n, 1 ≤ y-x-1 ≤ n)

// 출력
// x번째 수와 y번째 수가 같은 길이 2n의 랭퍼드 수열의 개수를 출력한다.

// 예제 입력 1 
// 3 1 5
// 예제 출력 1 
// 1
// 예제 입력 2 
// 7 4 10
// 예제 출력 2 
// 4
// 예제 입력 3 
// 12 1 3
// 예제 출력 3 
// 19776

#include <vector>
#include <iostream>

using namespace std;

int count = 0;

void rang(vector<int> series, vector<int> numset) {
    if (numset.size()==0) {count++; return;}
    for (int idx = 0; idx < numset.size(); idx++) {
        int num = numset[idx];
        // 빈자리 찾기
        int seat = 0;
        while (true) {
            if (series[seat] == 0) break;
            seat++;
        }
        if (seat + num + 1 >= series.size() || series[seat+num+1] != 0) continue;
        vector<int> new_series(series.size());
        for (int i = 0; i < series.size(); i++) {
            if (i == seat || i == seat+num+1) new_series[i] = num;
            else new_series[i] = series[i];
        }
        vector<int> new_numset;
        for (int i = 0; i < numset.size(); i++) {
            if (i == idx) continue;
            new_numset.push_back(numset[i]);
        }
        rang(new_series, new_numset);
    }
}

int main() {
///////////////////////////////////
int n, x, y; cin >> n >> x >> y;
x -= 1; y -= 1;
int fixed = y-x-1;
vector<int> numset;
for (int i = 1; i <= n; i++) {
    if (i == fixed) continue;    
    numset.push_back(i);
}
vector<int> series(2*n,0);
series[x] = fixed; series[y] = fixed;
rang(series, numset);
cout << count;
///////////////////////////////////
return 0;}