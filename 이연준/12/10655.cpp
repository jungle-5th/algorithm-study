/// BOJ 10655 마라톤 1

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    int N;  cin >> N;
    vector<pair<int, int>> checkpoint;
    for(int i = 0; i < N; i++) {
        int x, y;   cin >> x >> y;
        checkpoint.push_back({x, y});
    }
    vector<vector<int>> dp(N, vector<int>(2, 0));
    for(int i = 0; i < N - 1; i++) {
        dp[i][0] = abs(checkpoint[i + 1].first - checkpoint[i].first) + abs(checkpoint[i + 1].second - checkpoint[i].second);       // checkpoint 스킵하지 않은 경우
        if(i != N - 2) {
            dp[i][1] = abs(checkpoint[i + 2].first - checkpoint[i].first) + abs(checkpoint[i + 2].second - checkpoint[i].second);   // i번 checkpoint기준 자기 다음 스킵한 경우
        }
    }
    for(int i = 0; i < N - 1; i++) {
        cout << i << " to " << i + 1 << " : " << dp[i][0] << "\n";
        if(i != N - 2)  cout << i << " to " << i + 2 << " : " << dp[i][1] << "\n";
    }
    int total = 0;
    for(int i = 0; i < N; i++) {
        total += dp[i][0];
    }
    int saveD = 0;
    for(int i = 0; i < N - 2; i++) {
        saveD = max(saveD, dp[i][0] + dp[i + 1][0] - dp[i][1]);
    }
    cout << total - saveD;

    return 0;
}