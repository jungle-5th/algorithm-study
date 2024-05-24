/// BOJ 비트코인은 신이고 나는 무적이다

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N, M;
vector<int> chart;

int main() {
    cin >> N >> M;
    for(int i = 0; i < N; i++) {
        int money;  cin >> money;
        if(money < 0) {
            chart.push_back(-money);
        }
        else {
            chart.push_back(money);
        }
    }
    vector<vector<bool>> upbit(M, vector<bool>(1024, false));
    for(int i = 0; i < N; i++) {
        upbit[0][chart[i]] = true;
    }

    for(int i = 1; i < M; i++) {
        for(int j = 0; j < endpoint + 1; j++) {
            if(!upbit[i - 1][j])    continue;
            
            for(int k = 0; k < N; k++) {
                upbit[i][j ^ chart[k]] = true;
            }
        }
    }
    
    for(int i = 1023; i >= 0; i--) {
        if(upbit[M - 1][i]) {
            cout << i;
            return 0;
        }
    }

    return 0;
}