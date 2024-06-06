/// BOJ 2636 치즈

#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<vector<int>> map(100, vector<int>(100, 0));
vector<pair<int, int>> cheese;

int main() {
    cin >> N >> M;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> map[i][j];
            if(map[i][j])   cheese.push_back({i, j});
        }
    }
    

    return 0;
}