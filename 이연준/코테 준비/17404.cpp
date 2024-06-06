/// BOJ 17404 RGB거리 2

#include <iostream>
#include <vector>

using namespace std;

int N, M;

int main() {
    vector<vector<int>> coloring(N, vector<int>(M));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            cin >> coloring[i][j];
        }
    }
    

    return 0;
}