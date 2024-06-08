/// BOJ 1956 운동

#include <iostream>
#include <vector>
#define INF 1e9

using namespace std;

int V, E;

int main() {
    cin >> V >> E;
    vector<vector<int>> map(V + 1, vector<int>(V + 1, INF));
    for(int i = 0; i < E; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        map[a][b] = c;
    }

    for(int i = 1; i <= V; i++) {
        for(int j = 1; j <= V; j++) {
            for(int k = 1; k <= V; k++) {
                map[i][j] = min(map[i][j], map[i][k] + map[k][j]);
            }
        }
    }
    
    int ans = INF;
    for(int i = 1; i <= V; i++) {
        ans = min(ans, map[i][i]);
    }
    if(ans == INF) {
        cout << -1;
    }
    else {
        cout << ans;
    }
    return 0;
}