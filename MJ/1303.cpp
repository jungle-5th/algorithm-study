// https://www.acmicpc.net/problem/1303
// 전쟁 - 전투

// 문제
// 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다.
// 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다.
// 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
// N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가?
// 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

// 입력
// 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다.
// 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다.
// 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

// 출력
// 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

// 예제 입력 1 
// 6 5
// WBWWWB
// WWWWWB
// BBBBBW
// BBBWWB
// WWWWWB
// 예제 출력 1 
// 131 73

#include <vector>
#include <iostream>
#include <queue>
using namespace std;

int horizontal, vertical;
vector<pair<int,int>> direction = {{-1,0},{1,0},{0,-1},{0,1}};

int check(pair<int,int> start, char side, vector<string> *map) {
    queue<pair<int,int>> visit;
    visit.push(start);
    int count = 1;
    (*map)[start.first][start.second] = 'X';
    while (!visit.empty()) {
        pair<int,int> cord = visit.front();
        visit.pop();
        for (int d = 0; d < 4; d++) {
            int y = cord.first + direction[d].first;
            int x = cord.second + direction[d].second;
            if ((y < 0) || (y >= vertical) || (x < 0) || (x >= horizontal)) continue;
            if ((*map)[y][x] == side) {
                (*map)[y][x] = 'X';
                visit.push({y,x});
                count++;
            }
        }
    }
    return count*count;
}

int main() {
ios_base :: sync_with_stdio(false);
cin.tie();
//////////////////////////////////////////////
cin >> horizontal >> vertical;
vector<string> map(vertical);
for (int v = 0; v < vertical; v++) cin >> map[v];

int blue = 0, white = 0;

for (int y = 0; y < vertical; y++) {
    for (int x = 0; x < horizontal; x++) {
        if (map[y][x] == 'B') blue += check({y,x}, 'B', &map);
        else if (map[y][x] == 'W') white += check({y,x}, 'W', &map);
    }
}

cout << white << " " << blue;
//////////////////////////////////////////////
return 0;}