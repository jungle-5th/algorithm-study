/// BOJ 14620 꽃길

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int DirX[4] = {0, 0, 1, -1};
int DirY[4] = {1, -1, 0, 0};
int N;
vector<vector<int>> pot;

void makeCant(int x, int y, vector<vector<bool>> &can) {
    int sz = can.size();
    can[x][y] = false;
    if(x + 1 < sz && x + 1 >= 0 && y + 1 < sz && y + 1 >= 0) {
        can[x + 1][y + 1] = false;
    }
    if(x + 1 < sz && x + 1 >= 0 && y - 1 < sz && y - 1 >= 0) {
        can[x + 1][y - 1] = false;
    }
    if(x - 1 < sz && x - 1 >= 0 && y + 1 < sz && y + 1 >= 0) {
        can[x - 1][y + 1] = false;
    }
    if(x - 1 < sz && x - 1 >= 0 && y - 1 < sz && y - 1 >= 0) {
        can[x - 1][y - 1] = false;
    }
    
    for(int i = 0; i < 4; i++) {
        int nx = x + DirX[i];
        int nx2 = x + 2 * DirX[i];
        int ny = y + DirY[i];
        int ny2 = y + 2 * DirY[i];
        
        if(nx >= sz || nx < 0 || ny >= sz || ny < 0)    continue;
        can[nx][ny] = false;
        if(nx2 >= sz || nx2 < 0 || ny2 >= sz || ny2 < 0)    continue;
        can[nx2][ny2] = false;
    }
}

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        vector<int> tmp;
        for(int j = 0; j < N; j++) {
            int G;  cin >> G;
            tmp.push_back(G);
        }
        pot.push_back(tmp);
    }
    int answer = 0;
    vector<vector<int>> cost(N - 2, vector<int>(N - 2, 0));
    vector<vector<bool>> can(N - 2, vector<bool>(N - 2, true));
    for(int i = 1; i < N - 1; i++) {
        for(int j = 1; j < N - 1; j++) {
            cost[i - 1][j - 1] = pot[i][j] + pot[i - 1][j] + pot[i][j - 1] + pot[i + 1][j] + pot[i][j + 1];
        }
    }
    priority_queue<pair<int, pair<int, int>>> toPick;
    for(int i = 0; i < N - 2; i++) {
        for(int j = 0; j < N - 2; j++) {
            toPick.push({-cost[i][j], {i, j}});
        }
    }
    int flower = 3;
    while(flower--) {
        int x = toPick.top().second.first;
        int y = toPick.top().second.second;
        int CurCost = -toPick.top().first;
        while(!can[x][y]) {
            CurCost = -toPick.top().first;
            x = toPick.top().second.first;
            y = toPick.top().second.second;
            toPick.pop();
        }
        answer += CurCost;
        makeCant(x, y, can);
    }
    cout << answer;

    return 0;
}