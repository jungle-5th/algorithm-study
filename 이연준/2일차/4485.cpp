//// BOJ 4485 녹색 옷 입은 애가 젤다죠?

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int Dir_X[4] = {0, 0, 1, -1};
int Dir_Y[4] = {1, -1, 0, 0};

int bfs(int N, vector<vector<int>> cave) {
    priority_queue<pair<int, pair<int, int>>> rupee;
    vector<vector<bool>> visited(N, vector<bool>(N, false));
    rupee.push({-cave[0][0], {0, 0}});
    visited[0][0] = true;
    int answer = 0;
    while(!rupee.empty()) {
        int cr = -rupee.top().first;
        int cx = rupee.top().second.first;
        int cy = rupee.top().second.second;
        rupee.pop();

        if(cx == N - 1 && cy == N - 1) {
             answer = cr;
             break;
        }

        for(int i = 0; i < 4; i++) {
            int nx = cx + Dir_X[i];
            int ny = cy + Dir_Y[i];
            if(nx >= N || nx < 0 || ny >= N || ny < 0)    continue;
            if(visited[nx][ny]) continue;
            int nr = cave[nx][ny];
            visited[nx][ny] = true;
                
            rupee.push({-(cr + nr), {nx, ny}});
        }
    }
    return answer;
}

int main() {
    int num = 1;
    while(1) {
        int N;  cin >> N;
        if(N == 0)  break;
        vector<vector<int>> cave(N, vector<int>(N, 0));
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                cin >> cave[i][j];
            }
        }
        cout << "Problem " << num++ <<": ";
        cout << bfs(N, cave);
        cout << endl;
    }

    return 0;
}