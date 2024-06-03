/// BOJ 2589 보물섬

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
vector<vector<int>> map(50, vector<int>(50, -1));
vector<pair<int, int>> L;
int MAX = 0;

int Dir_X[4] = {0, 0, 1, -1};
int Dir_Y[4] = {1, -1, 0, 0};

void bfs(int idx) {
    vector<vector<int>> visited(50, vector<int>(50, -1));
    int sx = L[idx].first, sy = L[idx].second;
    queue<pair<int, int>> next;

    next.push({sx, sy});
    visited[sx][sy] = 0;
    while(!next.empty()) {
        int cx = next.front().first;
        int cy = next.front().second;

        next.pop();

        for(int i = 0; i < 4; i++) {
            int nx = cx + Dir_X[i];
            int ny = cy + Dir_Y[i];

            if(nx < 0 || nx >= N || ny < 0 || ny >= M)  continue;
            if(map[nx][ny] == 0 || visited[nx][ny] >= 0)    continue;
            next.push({nx, ny});
            visited[nx][ny] = visited[cx][cy] + 1;
            MAX = max(MAX, visited[nx][ny]);
        }
    }
}

int main() {
    cin >> N >> M;
    for(int i = 0; i < N; i++) {
        string str; cin >> str;
        for(int j = 0; j < M; j++) {
            if(str[j] == 'W') {
                map[i][j] = 0;
            }
            else {
                map[i][j] = 1;
                L.push_back({i, j});
            }
        }
    }
    for(int i = 0; i < L.size(); i++) {
        bfs(i);
    }
    cout << MAX;
    return 0;
}