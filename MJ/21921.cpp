// https://www.acmicpc.net/problem/21921
// 블로그

// 문제
// 찬솔이는 블로그를 시작한 지 벌써 N일이 지났다.
// 요즘 바빠서 관리를 못 했다가 방문 기록을 봤더니 벌써 누적 방문 수가 6만을 넘었다.
// 찬솔이는 X일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.
// 찬솔이를 대신해서 X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.

// 입력
// 첫째 줄에 블로그를 시작하고 지난 일수 N와 X가 공백으로 구분되어 주어진다.
// 둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.

// 출력
// 첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다. 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
// 만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.

// 예제 입력 1 
// 5 2
// 1 4 2 5 1
// 예제 출력 1 
// 7
// 1
// 예제 입력 2 
// 7 5
// 1 1 1 1 1 5 1
// 예제 출력 2 
// 9
// 2
// 예제 입력 3 
// 5 3
// 0 0 0 0 0
// 예제 출력 3 
// SAD

#include <iostream>
#include <vector>
using namespace std;

int main() {
ios_base::sync_with_stdio(false);
cin.tie(NULL);
/////////////////////////////////////////////////////
int n, x; cin >> n >> x;

vector<int> sum(n+1,0);
for (int i = 1; i <= n; i++) {
    int today; cin >> today;
    sum[i] = sum[i-1]+today;
}
pair<int, int> max = {0,0};
for (int i = x; i <= n; i++) {
    int rangeSum = sum[i]-sum[i-x];
    if (rangeSum == max.first) max.second+=1;
    else if(rangeSum > max.first) max = {rangeSum,1};
}
if (max.first) cout << max.first << "\n" << max.second;
else cout << "SAD";
/////////////////////////////////////////////////////
return 0;}