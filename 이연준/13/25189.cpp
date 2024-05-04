/// BOJ 25189 시니컬한 개구리

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
int fx, fy, hx, hy;
int DirX[4] = {0, 0, 1, -1};
int DirY[4] = {-1, 1, 0, 0};

int bfs(vector<vector<int>> map) {
    vector<vector<pair<int, int>>> visited(N, vector<pair<int, int>>(M, {0, 0}));
    queue<pair<pair<int, int>, int>> loc;                                           // 현재 위치, 어떻게 왔는지(점프로 or 개구리 밥으로)
    queue<int> num;
    visited[fx - 1][fy - 1].first = 1;
    loc.push({{fx - 1, fy - 1}, 0});
    num.push(0);

    while(!loc.empty()) {
        int cx = loc.front().first.first;
        int cy = loc.front().first.second;
        int jumped = loc.front().second;
        int cn = num.front();

        loc.pop();
        num.pop();

        if(cx == hx - 1 && cy == hy - 1) {
            return cn;
        }
        // 밥 무시 점프를 어떻게 넣음?
        int cj = map[cx][cy];
        if(cj == 0) continue;

        for(int i = 0; i < 4; i++) {
            int nx = cx + DirX[i] * cj;
            int ny = cy + DirY[i] * cj;

            if(nx >= N || nx < 0 || ny >= M || ny < 0)  continue;
            if(visited[nx][ny].first) continue;

            visited[nx][ny].first = 1;
            loc.push({{nx, ny}, jumped});
            num.push(cn + 1);
        }
        if(!jumped) {
            for(int i = 0; i < 4; i++) {                // 닿을 수 있는 모든 곳 점프시킴
                int nx = cx, ny = cy;   
                while(nx < N && nx >= 0 && ny < M && ny >= 0) {
                    nx += DirX[i];
                    ny += DirY[i];
                    if(visited[nx][ny].second)  continue;

                    visited[nx][ny].second = 1;                    
                    loc.push({{nx, ny}, 1});
                    num.push(cn + 1);
                }
            }
        }
    }
    return -1;
}

int main() {
    cin >> N >> M;
    cin >> fx >> fy >> hx >> hy;
    vector<vector<int>> map(N, vector<int>(M, 0));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> map[i][j];
        }
    }
    if(fx == hx && fy == hy)    cout << 0;
    else    cout << bfs(map);

    return 0;
}