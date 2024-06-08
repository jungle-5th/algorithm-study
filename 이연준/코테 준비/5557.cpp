/// BOJ 5557 1학년

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> num(N);
    for(int i = 0; i < N; i++) {
        cin >> num[i];
    }
    vector<vector<long long>> dp(N - 1, vector<long long>(21, 0));
    dp[0][num[0]] = 1;
    for(int i = 1; i < N - 1; i++) {
        for(int j = 0; j <= 20; j++) {
            if(dp[i - 1][j]) {              // i - 1 번째 수까지 더했을 때 j가 되는 결과가 있는 경우
                if(j >= num[i]) {
                    dp[i][j - num[i]] += dp[i - 1][j];      // j - (i번째 숫자) >= 0 일 때, i번째까지 계산한 결과로 더해짐
                }
                if(j + num[i] <= 20) {      // j + (i번째 숫자) <= 20 일 때, i번째까지 계산한 결과로 더해짐
                    dp[i][j + num[i]] += dp[i - 1][j];
                }
            }
        }
    }
    cout << dp[N - 2][num[N - 1]];

    return 0;
}