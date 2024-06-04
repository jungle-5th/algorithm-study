/// BOJ 2206 벽 부수고 이동하기

#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int N, M;
vector<vector<int>> map;
vector<vector<bool>> visited1(1000, vector<bool>(1000, false));
vector<vector<bool>> visited2(1000, vector<bool>(1000, false));
int MIN = 999999999;

int DirX = {0, 0, 1, -1};
int DirY = {1, -1, 0, 0};

void bfs() {
    queue<pair<pair<int, int>, bool>> next;
    queue<int> dist;

    next.push({{0, 0}, false});
    dist.push(1);

    while(!next.empty()) {
        int cx = next.front().first.first;
        int cy = next.front().first.second;
        bool crash = next.front().second;

        int cd = dist.front();

        next.pop();
        dist.pop();

        if(cx == N - 1 && cy == M - 1) {
            MIN = min(MIN, cd);
        }

        for(int i = 0; i < 4; i++) {
            int nx = cx + DirX[i];
            int ny = cy + DirY[i];

            if(nx >= N || nx < 0 || ny >= M || ny < 0)  continue;
            
        }
    }
}

int main() {
    cin >> N >> M;
    map.resize(N);
    for(int i = 0; i < N; i++) {
        string str; cin >> str;
        vector<int> tmp;
        for(int j = 0; ; j < M; j++) {
            if(str[j] == '0') {
                tmp.push_back(0);
            }
            else {
                tmp.push_back(1);
            }
        }
        map[i] = tmp;
    }


    return 0;
}