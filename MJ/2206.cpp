// https://www.acmicpc.net/problem/2206
// 벽 부수고 이동하기

// 문제
// N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
// 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
// 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
// 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
// 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
// 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

// 출력
// 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

// 예제 입력 1 
// 6 4
// 0100
// 1110
// 1000
// 0000
// 0111
// 0000
// 예제 출력 1 
// 15
// 예제 입력 2 
// 4 4
// 0111
// 1111
// 1111
// 1110
// 예제 출력 2 
// -1

#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

vector<string> map;
queue<pair<int, int>> que;
queue<pair<int, int>> secondwind;

int main() {
/////////////////////////////////////////////////
int n_of_row, m_of_column;
cin >> n_of_row >> m_of_column;
// make map
string inputrow;
for (int n = 0; n < n_of_row; n++) {
    cin >> inputrow;
    map.push_back(inputrow);
}

// make visited map of {visited, coin}
vector<vector<int>> visitedmap(n_of_row, vector<int>(m_of_column, 0));
visitedmap[0][0] = 1;
que.push({0,0});

vector<pair<int,int>> direction = {{-1,0}, {1,0}, {0,-1}, {0,1}};
while(!que.empty()) {
    pair<int, int> cord = que.front();
    que.pop();
    for(int d = 0; d < 4; d++) {
        int y = cord.first + direction[d].first;
        int x = cord.second + direction[d].second;
        // if not valid cord, pass
        if (y < 0 || y >= n_of_row) continue;
        if (x < 0 || x >= m_of_column) continue;
        // if visited, pass
        if (visitedmap[y][x] != 0) continue;

        if (map[y][x] == '0') {
            visitedmap[y][x] = visitedmap[cord.first][cord.second] + 1;
            que.push({y,x});
        }
        else if (map[y][x] == '1') {
            visitedmap[y][x] = visitedmap[cord.first][cord.second] + 1;
            secondwind.push({y,x});
        }
    }
}

while(!secondwind.empty()) {
    pair<int, int> cord = secondwind.front();
    secondwind.pop();
    for(int d = 0; d < 4; d++) {
        int y = cord.first + direction[d].first;
        int x = cord.second + direction[d].second;
        // if not valid cord, pass
        if (y < 0 || y >= n_of_row) continue;
        if (x < 0 || x >= m_of_column) continue;

        if (map[y][x] == '0') {
            if (visitedmap[y][x] == 0 || visitedmap[y][x] > (visitedmap[cord.first][cord.second]+1)) {
                visitedmap[y][x] = visitedmap[cord.first][cord.second] + 1;
                secondwind.push({y,x});
            }
        } 
    }
}

if (visitedmap[n_of_row-1][m_of_column-1] == 0) cout << -1;
else cout << (visitedmap[n_of_row-1][m_of_column-1]);

/////////////////////////////////////////////////
return 0;}