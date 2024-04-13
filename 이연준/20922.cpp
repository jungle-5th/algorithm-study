// BOJ 20922

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int N, K;
vector<int> num;

int main() {
    cin >> N >> K;
    map<int, int> cnt;
    for(int i = 0; i < N; i++) {
        int tmp;    cin >> tmp;
        num.push_back(tmp);
        cnt[tmp] = 0;
    }
    if(N == 1) {
        cout << 1;
        return 0;
    }
    int maxl = 2;
    int l = 0, r = 1;
    cnt[num[l]] += 1;
    cnt[num[r]] += 1;
    if(num[l] == num[r] && K == 1) {
        l = 1;
        cnt[num[l]] -= 1;
        maxl = 1;
    }

    while(r < N - 1) {
        if(cnt[num[r + 1]] < K) {
            r++;
            cnt[num[r]] += 1;
            maxl = max(maxl, r - l + 1);
        }
        else {
            r++;
            cnt[num[r]] += 1;
            while(cnt[num[r]] > K) {
                cnt[num[l]] -= 1;
                l++;
            }
            maxl = max(maxl, r - l + 1);
        }
    }
    cout << maxl;
    return 0;
}
