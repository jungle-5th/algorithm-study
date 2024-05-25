// https://www.acmicpc.net/problem/23257
// 비트코인은 신이고 나는 무적이다

#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
////////////////////////////////////////
int n, m;
cin >> n >> m;

set<int> wolbong, add;
int maxval = 0;
for (int i = 0; i < n; i++) {
    int w;
    cin >> w;
    wolbong.insert(abs(w));
    if (maxval < abs(w)) maxval = abs(w);
}

// m이 1인경우
if (m == 1) {
    cout << maxval;
    return 0;
}

set<int>::iterator itr1, itr2;
for (int i = 0; i < m; i++) {
    maxval = 0;
    for (itr1 = wolbong.begin(); itr1 != wolbong.end() ; ++itr1) {
        for (itr2 = itr1;  itr2 != wolbong.end(); ++itr2) {
            int val = *itr1 ^ *itr2;
            add.insert(val);
            if (maxval < val) maxval = val;
        }    
    }
    if ((maxval) & (maxval+1) == 0) break;
    int sizeofset = wolbong.size();
    wolbong.insert(add.begin(), add.end());
    if (sizeofset == wolbong.size()) break;
}

cout << maxval;
////////////////////////////////////////
return 0;}