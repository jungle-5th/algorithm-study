// https://www.acmicpc.net/problem/17485
// 진우의 달 여행

// 문제
// 우주비행이 꿈이였던 진우는 음식점 '매일매일싱싱'에서 열심히 일한 결과 달 여행에 필요한 자금을 모두 마련하였다!
// 지구와 우주사이는 N X M 행렬로 나타낼 수 있으며 각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료의 양이다.
// 진우는 여행경비를 아끼기 위해 조금 특이한 우주선을 선택하였다. 진우가 선택한 우주선의 특징은 아래와 같다.
// 1. 지구 -> 달로 가는 경우 우주선이 움직일 수 있는 방향은 아래, 좌하 대각선, 우하 대각선이다.
// 2. 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다.
// 진우의 목표는 연료를 최대한 아끼며 지구의 어느위치에서든 출발하여 달의 어느위치든 착륙하는 것이다.
// 최대한 돈을 아끼고 살아서 달에 도착하고 싶은 진우를 위해 달에 도달하기 위해 필요한 연료의 최소값을 계산해 주자.

// 입력
// 첫줄에 지구와 달 사이 공간을 나타내는 행렬의 크기를 나타내는 N, M (2 ≤ N, M ≤ 1000)이 주어진다.
// 다음 N줄 동안 각 행렬의 원소 값이 주어진다. 각 행렬의 원소값은 100 이하의 자연수이다.

// 출력
// 달 여행에 필요한 최소 연료의 값을 출력한다.

// 예제 입력 1 
// 6 4
// 5 8 5 1
// 3 5 8 4
// 9 77 65 5
// 2 1 5 2
// 5 98 1 5
// 4 95 67 58
// 예제 출력 1 
// 29

#include <vector>
#include <iostream>
#define INF 2000000000
using namespace std;

struct dpElement {
    int ld, d, rd;
};

int main() {
////////////////////////////////////////
int vertical, horizontal; cin >> vertical >> horizontal;
vector<vector<int>> map(vertical, vector<int>(horizontal+2, 0));
for (int v = 0; v < vertical; v++) { // map 만들기
    map[v][0] = INF;
    for (int h = 1; h <= horizontal; h++) {
        cin >> map[v][h];
    }
    map[v][horizontal+1] = INF;
}

vector<vector<dpElement>> dptable(vertical, vector<dpElement>(horizontal+2));
for (int h = 0; h <= horizontal+1; h++) dptable[0][h] = {map[0][h],map[0][h],map[0][h]};
for (int v = 1; v < vertical; v++) {
    dptable[v][0] = {INF,INF,INF};
    for (int h = 1; h <= horizontal; h++) {
        dptable[v][h].ld = min<int>(dptable[v-1][h+1].d,dptable[v-1][h+1].rd) + map[v][h];
        dptable[v][h].d = min<int>(dptable[v-1][h].ld,dptable[v-1][h].rd) + map[v][h];
        dptable[v][h].rd = min<int>(dptable[v-1][h-1].ld,dptable[v-1][h-1].d) + map[v][h];
    }
    dptable[v][horizontal+1] = {INF,INF,INF};
}
int minval = INF;
for (int h = 1; h <=horizontal; h++) {
    if (dptable[vertical-1][h].ld < minval) minval = dptable[vertical-1][h].ld;
    if (dptable[vertical-1][h].d < minval) minval = dptable[vertical-1][h].d;
    if (dptable[vertical-1][h].rd < minval) minval = dptable[vertical-1][h].rd;
}
cout << minval;
////////////////////////////////////////
return 0;}