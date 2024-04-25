/// 15486 퇴사 2

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int N;  cin >> N;
    vector<vector<int>> task(N + 1, vector<int>(2));
    for(int i = 1; i <= N; i++) {
        cin >> task[i][0] >> task[i][1];
    }
    // map<int, int> money;
    // for(int i = 1; i <= N + 1; i++) {
    //     money[i] = 0;
    // }
    vector<int> dp(N + 2, 0);
    for(int i = 1; i <= N + 1; i++) {
        // cout << i << "일째의 최대 값을 찾음\n";
        int ithmax;
        if(i == 1) {
            ithmax = 0;
        }
        else {
            ithmax = max(dp[i - 1], dp[i]);
        }
        dp[i] = ithmax;
        // cout << dp[i] << endl;
        if(i <= N) {
            int nextday = i + task[i][0];
            int nextmoney = ithmax + task[i][1];
            if(nextday <= N + 1) {
                dp[nextday] = max(nextmoney, dp[nextday]);
            }
        }
    }
    cout << dp[N + 1];

    return 0;
}