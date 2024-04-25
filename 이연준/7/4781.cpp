/// BOJ 4781 사탕 가게

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    while(1) {
        int n;
        double m;
        cin >> n >> m;
        if(n == 0)  break;
        
        vector<pair<int, double>> candy;
        for(int i = 0; i < n; i++) {
            int c;
            double p;
            cin >> c >> p;
            candy.push_back({c, p});
        }

        int M = (int)(m * 100 + 0.5);
        vector<vector<int>> dp(n + 1, vector<int>(M + 1, 0));

        for(int i = 0; i < n; i++) {
            dp[i][0] = 0;
        }
        for(int i = 0; i < M; i++) {
            dp[0][i] = 0;
        }
        for(int i = 1; i < n + 1; i++) {
            for(int j = 0; j <= M; j++) {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                if(j - int(candy[i - 1].second * 100 + 0.5) >= 0) {
                    dp[i][j] = max(max(dp[i][j], dp[i - 1][j - int(candy[i - 1].second * 100 + 0.5)] + candy[i - 1].first), dp[i][j - int(candy[i - 1].second * 100 + 0.5)] + candy[i - 1].first);
                }
            }
        }
        cout << dp[n][M] << endl;
    }

    return 0;
}