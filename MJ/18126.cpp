// https://www.acmicpc.net/problem/18126
// 너구리 구구

// 문제
// 텔레토비 동산에 사는 너구리 구구는 입구, 거실, 주방, 안방, 공부방, 운동실, 음악실, 음식 창고 등 N개의 방을 가지고 있다.
// 입구를 포함한 모든 방은 1부터 N까지의 번호가 있고, 입구는 1번이다.  구구의 집으로 들어가는 입구는 한 개이며 입구과 모든 방들은 총 N-1개의 길로 서로 오고 갈 수 있다.
// 구구는 스머프 동산에서 멜론아 아이스크림을 발견했다. 구구는 무더운 여름 햇살을 피해 최대한 입구에서 먼 방에 아이스크림을 숨기려고 한다.
// 구구가 집 입구에서 멜론아 아이스크림을 숨기려고 하는 방까지 이동하는 거리를 구하여라.

// 입력
// 첫째 줄에 정수 N(1 ≤ N ≤ 5,000)이 주어진다.
// 다음 N-1개의 줄에 구구의 집의 모든 길의 정보가 정수 A, B, C(1 ≤ A, B ≤ N, 1 ≤ C ≤ 1,000,000,000)로 주어진다.
// A번 방과 B번 방 사이를 양방향으로 연결하는 길의 길이가 C임을 의미한다.

// 출력
// 구구가 집 입구에서 멜론아 아이스크림을 숨기려고 하는 방까지 이동하는 거리를 구하여라.

// 예제 입력 1 
// 4
// 1 2 3
// 2 3 2
// 2 4 4
// 예제 출력 1 
// 7

#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <climits>
using namespace std;

int main() {
ios_base :: sync_with_stdio(false); 
cin.tie(NULL); 
////////////////////////////////////////////
int n_of_rooms;
long long a, b, c;

cin >> n_of_rooms;

// make adjlist
vector<long long> adjlist(n_of_rooms, LLONG_MAX);
adjlist[0] = 0;
queue<vector<long long>> que;
for (int n = 0; n < n_of_rooms-1; n++) {
    cin >> a >> b >> c;
    if (a == 1) adjlist[b-1] = c;
    else {
        que.push({a-1, b-1, c});
        que.push({b-1, a-1, c});
    }
}

while (!que.empty()) {
    long long rm1 = que.front()[0];
    long long rm2 = que.front()[1];
    long long dist = que.front()[2];
    if (adjlist[rm1] == LLONG_MAX) que.push({rm1,rm2,dist});
    else if (adjlist[rm2] > adjlist[rm1] + dist) adjlist[rm2] = adjlist[rm1] + dist;
    que.pop();
}

long long maxdist = 0;
for (int n = 1; n < n_of_rooms; n++) {
    if (maxdist < adjlist[n]) maxdist = adjlist[n];
}

cout << maxdist;
////////////////////////////////////////////
return 0;}