/// BOJ 11057 오르막 수

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> dp(N + 1, vector<int>(10, 0));
    for(int i = 0; i < 9; i++) {
        dp[0][i] = 0;
        dp[1][i] = 1;
    }
    for(int i = 2; i <= N; i++) {
        int tot = 0;
        for(int j = 9; j >= 0; j--) {
            tot += dp[i - 1][j];
            dp[i][j] % 10007 = tot;
        }
    }
    int ans = 0;
    for(int i = 0; i <= 9; i++) {
        ans += dp[N][i] % 10007;
    }
    cout << ans % 10007;

    return 0;
}