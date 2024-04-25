//// BOJ 7562 나이트의 이동

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int Dir_X[8] = {-2, -2, -1, 1, 2, 2, 1, -1};
int Dir_Y[8] = {-1, 1, 2, 2, 1, -1, -2, -2};

int main() {
    int T;  cin >> T;
    while(T--) {
        int l;  cin >> l;
        vector<vector<int>> chess(l, vector<int>(l, 0));
        vector<vector<bool>> visited(l, vector<bool>(l, false));
        int sx, sy;
        cin >> sx >> sy;
        int ex, ey;
        cin >> ex >> ey;

        queue<pair<int, int>> node;
        queue<int> num;
        node.push({sx, sy});
        num.push(0);
        visited[sx][sy] = true;
        while(!node.empty()) {
            int cx = node.front().first;
            int cy = node.front().second;
            int cn = num.front();

            node.pop();
            num.pop();

            if(cx == ex && cy == ey) {
                cout << cn << "\n";
                break;
            }

            for(int i = 0; i < 8; i++) {
                int nx = cx + Dir_X[i];
                int ny = cy + Dir_Y[i];

                if(nx >= l || nx < 0 || ny >= l || ny < 0)  continue;
                if(visited[nx][ny]) continue;

                node.push({nx, ny});
                num.push(cn + 1);
                visited[nx][ny] = true;
            }
        }
    }
    return 0;
}