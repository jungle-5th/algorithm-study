// https://www.acmicpc.net/problem/2589
// 보물섬

// 문제
// 보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
// 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다.
// 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
// 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.
// 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에는 보물 지도의 세로의 크기와 가로의 크기가 빈칸을 사이에 두고 주어진다.
// 이어 L과 W로 표시된 보물 지도가 아래의 예와 같이 주어지며, 각 문자 사이에는 빈 칸이 없다. 보물 지도의 가로, 세로의 크기는 각각 50이하이다.

// 출력
// 첫째 줄에 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력한다.

// 예제 입력 1 
// 5 7
// WLLWWWL
// LLLWLLL
// LWLWLWW
// LWLWLLL
// WLLWLWW
// 예제 출력 1 
// 8

#include <vector>
#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
////////////////////////////////////////////////////////////
int vertical, horizontal;
cin >> vertical >> horizontal;
int nodes = vertical*horizontal;
string strmap;
vector<vector<int>> map(nodes, vector<int>(nodes, 50000));
for (int i = 0; i < vertical; i++) {
    string str;
    cin >> str;
    strmap += str;
}
// cout << strmap;

vector<bool> lands(nodes, 0);
vector<vector<int>> adjlist(nodes);
for (int i = 0; i < nodes; i++) {
    if (strmap[i] == 'L') {
        lands[i] = 1;
    }
    else continue;
    int left = i+1;
    int down = i+horizontal;
    if ((left%horizontal != 0) && (strmap[left] == 'L')) {
        adjlist[i].push_back(left);
        adjlist[left].push_back(i);
    }
    if ((down < nodes) && (strmap[down] == 'L')) {
        adjlist[i].push_back(down);
        adjlist[down].push_back(i);
    }
}

// bfs

int maxval = 0;

for (int i = 0; i < nodes; i++) {
    if (lands[i] == 0) continue; // 물이면 스킵
    if (adjlist[i].empty()) continue;
    // 육지면 bfs 시작
    queue<int> que;
    vector<int> count(nodes, 0);
    for (int j = 0; j < adjlist[i].size(); j++) {
        que.push(adjlist[i][j]);
        count[adjlist[i][j]] = 1;
    }
    count[i] = 1;

    int lastland;
    int result;
    while (!que.empty())
    {
        lastland = que.front();
        result = count[lastland];
        que.pop();
        for (int j = 0; j < adjlist[lastland].size(); j++) {
            int candidate = adjlist[lastland][j];
            if (count[candidate] == 0) {
                que.push(candidate);
                count[candidate] = count[lastland] +1;
            }
        }
    }
    /*
    // lastland 기준으로 다시한번 bfs
    lands[lastland] = 0;
    for (int i = 0; i < nodes; i++) count[i] = 0;
    for (int j = 0; j < adjlist[i].size(); j++) {
        que.push(adjlist[lastland][j]);
        count[adjlist[lastland][j]] = 1;
    }
    while (!que.empty())
    {
        lastland = que.front();
        result = count[lastland];
        lands[lastland] = 0;
        que.pop();
        for (int j = 0; j < adjlist[lastland].size(); j++) {
            int candidate = adjlist[lastland][j];
            if (count[candidate] == 0) {
                que.push(candidate);
                count[candidate] = count[lastland] +1;
            }
        }
    }
    */
    if (maxval < result) maxval = result;
}

cout << maxval;
////////////////////////////////////////////////////////////
return 0;}