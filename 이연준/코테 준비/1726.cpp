/// BOJ 1726 로봇

#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int M, N;
vector<vector<int>> factory(100, vector<int>(100));
vector<int> start(3);
vector<int> arrive(3);
vector<vector<vector<bool>>> visited(4, vector<vector<bool>>(100, vector<bool>(100, false)));
int DirX[4] = {0, 0, 1, -1};
int DirY[4] = {1, -1, 0, 0};

bool Check(int d, int x, int y) {
    if(x >= M || x < 0 || y >= N || y < 0)  return true;
    if(factory[x][y])   return true;
    if(visited[d][x][y])    return true;
    
    return false;
}

int turn_left(int d) {
    switch(d) {
        case 0:
            return 3;
            break;
        case 1:
            return 2;
            break;
        case 2:
            return 0;
            break;
        case 3:
            return 1;
            break;
    }
}

int turn_right(int d) {
    switch(d) {
        case 0:
            return 2;
            break;
        case 1:
            return 3;
            break;
        case 2:
            return 1;
            break;
        case 3:
            return 0;
            break;
    }
}

int GetOrder() {
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push({{start[0], start[1]}, {start[2], 0}});        // cx, cy, cd, co
    visited[start[2]][start[0]][start[1]] = true;

    while(!q.empty()) {
        int cx = q.front().first.first;
        int cy = q.front().first.second;
        int cd = q.front().second.first;
        int co = q.front().second.second;
        q.pop();
        cout << "현재 위치 : " << cx << ", " << cy << endl;
        cout << "현재 방향 : " << cd << endl;
        cout << "현재까지의 명령 횟수 : " << co << endl;
        if(cx == arrive[0] && cy == arrive[1] && cd == arrive[2]) {
            return co;
        }

        for(int i = 1; i <= 3; i++) {
            int nx = cx + DirX[cd] * i;
            int ny = cy + DirY[cd] * i;

            if(Check(cd, nx, ny))   break;

            q.push({{nx, ny}, {cd, co + 1}});
            visited[cd][nx][ny] = true;
        }

        int nd1 = turn_left(cd);
        int nd2 = turn_right(cd);
        
        if(!visited[nd1][cx][cy]) {
            visited[nd1][cx][cy] = true;
            q.push({{cx, cy}, {nd1, co + 1}});
        }
        if(!visited[nd2][cx][cy]) {
            visited[nd2][cx][cy] = true;
            q.push({{cx, cy}, {nd2, co + 1}});
        }
    }
    return -1;
}

int main() {
    cin >> M >> N;
    for(int i = 0; i < M; i++) {
        for(int j = 0; j < N; j++) {
            cin >> factory[i][j];
        }
    }
    for(int i = 0; i < 3; i++) {
        cin >> start[i];
        start[i]--;
    }
    for(int i = 0; i < 3; i++) {
        cin >> arrive[i];
        arrive[i]--;
    }

    cout << GetOrder();

    return 0;
}