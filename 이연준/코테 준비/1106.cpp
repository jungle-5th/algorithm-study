/// BOJ 1106 호텔

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int C, N;
    cin >> C >> N;
    vector<vector<int>> money(N, vector<int>(2));
    int Max_money = 0;
    for(int i = 0; i < N; i++) {
        cin >> money[i][0] >> money[i][1];
        int m = C / money[i][1];
        if(m * money[i][1] < C) {
            m++;
        }
        Max_money = max(Max_money, m * money[i][0]);
    }
    vector<vector<int>> dp(N + 1, vector<int>(Max_money + 1, 0));
    vector<int> ans(N, Max_money);
    for(int i = 1; i <= N; i++) {
        int m = money[i - 1][0];
        int p = money[i - 1][1];
        for(int j = 1; j <= Max_money; j++) {
            if(j >= m) {
                dp[i][j] = max(max(dp[i - 1][j], dp[i - 1][j - m] + p), dp[i][j - m] + p);
            }
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
            if(dp[i][j] >= C) {
                ans[i - 1] = j;
                break;
            }
        }
    }
    cout << *min_element(ans.begin(), ans.end());

    return 0;
}