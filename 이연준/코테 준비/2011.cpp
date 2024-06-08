/// BOJ 2011 암호코드

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string str;
    cin >> str;

    vector<long long> dp(str.length() + 1, 0);
    if(str[0] == '0') {      // 암호문의 시작이 0이라면 잘못된 암호문이므로 0을 출력하고 return
        cout << 0;
        return 0;
    }
    else {
        dp[0] = 1;
        dp[1] = 1;           // 첫 문자는 0이 아니라면 해석할 수 있는 암호문의 개수가 1개임
        for(int i = 2; i < str.length() + 1; i++) {
            if(str[i - 1] >= '1' && str[i - 1] <= '9') {
                // i - 1 번째 문자가 0이 아니라면 이전 문자까지 봤을 때의 암호문의 개수와 같아짐
                dp[i] += dp[i - 1];
            }
            if("10" <= str.substr(i - 2, 2) && str.substr(i - 2, 2) <= "26") { 
            // 만약 이전 문자와 합쳤을 때, 10이상 26이하(다른 알파벳)라면 i - 2 번째 문자까지 봤을때 만큼 개수가 늘어남
                dp[i] += dp[i - 2];
            }
            dp[i] %= 1000000;
        }
        cout << dp[str.length()] % 1000000;
    }

    return 0;
}