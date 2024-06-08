/// BOJ 1600 말이 되고픈 원숭이

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> map(200, vector<int>(200));
vector<vector<vector<bool>>> visited(31, vector<vector<bool>>(200, vector<bool>(200, false)));
int K, W, H;
int DirX[4] = {0, 0, 1, -1};
int DirY[4] = {1, -1, 0, 0};
int jumpX[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
int jumpY[8] = {-2, -1, 1, 2, 2, 1, -1, -2};

int bfs() {
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push({{0, 0}, {K, 0}});
    visited[K][0][0] = true;
    int ret = -1;
    while(!q.empty()) {
        int cx = q.front().first.first;
        int cy = q.front().first.second;
        int ck = q.front().second.first;
        int num = q.front().second.second;
        q.pop();

        if(cx == H - 1 && cy == W - 1) {
            ret = num;
            break;
        }

        for(int i = 0; i < 4; i++) {
            int nx = cx + DirX[i];
            int ny = cy + DirY[i];

            if(nx < 0 || nx >= H || ny < 0 || ny >= W)  continue;
            if(visited[ck][nx][ny]) continue;
            if(map[nx][ny]) continue;
            q.push({{nx, ny}, {ck, num + 1}});
            visited[ck][nx][ny] = true;
        }

        if(ck == 0) continue;
        for(int i = 0; i < 8; i++) {
            int nx = cx + jumpX[i];
            int ny = cy + jumpY[i];

            if(nx < 0 || nx >= H || ny < 0 || ny >= W)  continue;
            if(visited[ck - 1][nx][ny]) continue;
            if(map[nx][ny]) continue;
            q.push({{nx, ny}, {ck - 1, num + 1}});
            visited[ck - 1][nx][ny] = true;
        }
    }
    return ret;
}

int main() {
    cin >> K;
    cin >> W >> H;
    for(int i = 0; i < H; i++) {
        for(int j = 0; j < W; j++) {
            cin >>map[i][j];
        }
    }
    cout << bfs();

    return 0;
}