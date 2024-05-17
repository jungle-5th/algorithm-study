/// BOJ 14627 파닭파닭

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int S, C;
vector<long long> SO;

long long binary_search(long long l, long long r) {
    long long MIN = 0;
    while(l <= r) {
        // cout << "l : " << l << ", r : " << r << endl;
        long long mid = (l + r) / 2;
        if(mid == 0) {
            l++;
            continue;
        }
        // cout << "mid : " << mid << endl;
        int make = 0;
        for(int i = 0; i < S; i++) {
            make += (SO[i] / mid);
        }
        // cout << "만들 수 있는 파닭 개수 : " << make << endl;
        if(make < C) {
            r = mid - 1;
        }
        else if(make > C) {
            l = mid + 1;
        }
        else {
            MIN = max(MIN, mid);
            l = mid + 1;
        }
    }
    return MIN;
}

int main() {
    cin >> S >> C;
    for(int i = 0; i < S; i++) {
        long long L;    cin >> L;
        SO.push_back(L);
    }
    sort(SO.begin(), SO.end());
    long long l = 0, r = SO[S - 1];
    long long length = binary_search(l, r);
    // cout << length << endl;
    long long ans = 0;
    for(int i = 0; i < S; i++) {
        ans += SO[i] % length;
    }
    cout << ans;

    return 0;
}