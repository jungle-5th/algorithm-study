/// BOJ 2811 상범이의 우울

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> feeling;
int maxlen = 0;
vector<int> maxStart;

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        int mental; cin >> mental;
        feeling.push_back(mental);
    }
    vector<int> minus(N + 1, 0);
    for(int i = 1; i <= N; i++) {
        if(feeling[i - 1] < 0) {
            minus[i] = minus[i - 1] + 1;
        }
    }
    maxlen = *max_element(minus.begin(), minus.end());
    for(int i = 1; i <= N; i++) {
        if(minus[i] == maxlen) {
            maxStart.push_back(i - 1);
        }
    }
    int ans = 0;
    for(int i = 0; i < maxStart.size(); i++) {          // maxlen 중 하나를 골라 3T만큼 꽃 주는 날짜 정함
        int give = 0;
        vector<bool> flower(N, false);
        int minus3T = maxStart[i] - maxlen * 3;
        for(int idx = minus3T; idx < maxStart[i]; idx++) {
            if(idx < 0) continue;

            flower[idx] = true;
            give++;
        }
        for(int j = 0; j < maxStart.size(); j++) {
            if(j == i)  continue;

            int minus2T = maxStart[j] - maxlen * 2;
            for(int idx = minus2T; idx < maxStart[j]; idx++) {
                if(idx < 0) continue;
                if(flower[idx]) continue;

                flower[idx] = true;
                give++;
            }
        }
        for(int i = 0; i < N; i++) {
            if(flower[i])   cout << 1 << " ";
            else            cout << 0 << " ";
        }
        cout << endl;
        ans = max(ans, give);
    }
    cout << ans;
    

    return 0;
}