// https://www.acmicpc.net/problem/14940
// 쉬운 최단거리

// 문제
// 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
// 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

// 입력
// 지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
// 다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다.
// 입력에서 2는 단 한개이다.

// 출력
// 각 지점에서 목표지점까지의 거리를 출력한다.
// 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

// 예제 입력 1 
// 15 15
// 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
// 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
// 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
// 예제 출력 1 
// 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
// 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
// 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
// 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
// 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
// 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
// 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
// 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
// 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
// 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
// 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
// 11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
// 12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
// 13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
// 14 15 16 17 18 19 20 21 22 23 0 31 32 33 34

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
ios_base::sync_with_stdio(false);
cin.tie(NULL);
/////////////////////////////////////////////////
int vertical, horizontal; cin >> vertical >> horizontal;
vector<vector<int>> map(vertical, vector<int>(horizontal,0));
vector<vector<int>> distance(vertical, vector<int>(horizontal, 100000000));
vector<pair<int,int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};
queue<pair<int,int>> visitq;
for (int v = 0; v < vertical; v++) {
    for (int h = 0; h < horizontal; h++) {
        int num; cin >> num;
        if (num == 0) {
            distance[v][h] = 0;
        } 
        else if (num == 2) {
            distance[v][h] = 0;
            visitq.push({v,h});
        }
        map[v][h] = num;
    }
}
while (!visitq.empty()) {
    int y = visitq.front().first;
    int x = visitq.front().second;
    int dist = distance[y][x];
    visitq.pop();
    for (int d = 0; d < 4; d++) {
        int newy = y + directions[d].first;
        int newx = x + directions[d].second;
        if (newy < 0 || newy >= vertical || newx < 0 || newx >= horizontal) continue;
        if (distance[newy][newx] == 0) continue;
        if (distance[newy][newx] > dist+1) {
            distance[newy][newx] = dist+1;
            visitq.push({newy,newx});
        }
    }
}

for (int v = 0; v < vertical; v++) {
    for (int h = 0; h < horizontal; h++) {
        int d = distance[v][h];
        if (d == 100000000) d = -1;
        cout << d << " ";
    }
    cout << "\n";
}
/////////////////////////////////////////////////
return 0;}