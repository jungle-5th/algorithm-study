///// BOJ 1976 여행 가자

#include <iostream>
#include <vector>

using namespace std;

int N, M;

int main() {
    cin >> N >> M;
    vector<vector<int>> edge(N, vector<int>(N, 0));
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cin >> edge[i][j];
        }
    }
    vector<int> route;
    for(int i = 0; i < M; i++) {
        int tmp;    cin >> tmp;
        route.push_back(tmp);
    }
    if(route.size() == 1) {
        cout << "YES";
        return 0;
    }
    for(int k = 0; k < N; k++) {
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                edge[i][j] = edge[i][j] || (edge[i][k] && edge[k][j]);
            }
        }
    }
    bool flag = true;
    int st = route[0] - 1;
    for(int i = 1; i < M; i++) {
        if(!edge[st][route[i] - 1]) {
            if(st == route[i] - 1)  continue;
            flag = false;
            break;
        }
    }
    if(flag)    cout << "YES";
    else        cout << "NO";

    return 0;
}