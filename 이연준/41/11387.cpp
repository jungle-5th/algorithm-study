/// BOJ 11387 님 무기가 좀 나쁘시네여

#include <iostream>
#include <vector>
#include <algorithm>
typedef unsigned long long ll;

using namespace std;

ll get_stat(ll a, ll s, ll cp, ll c, ll as) {
    return a * (100 + s) * ( (10000 - min(cp * 100, (ll)10000)) + min(cp, (ll)100) * c ) * (100 + as);
}

int main() {
    vector<vector<ll>> sw(4, vector<ll>(5, 0));

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 5; j++) {
            cin >> sw[i][j];
        }
    }
    ll cri_stat = get_stat(sw[0][0], sw[0][1], sw[0][2], sw[0][3], sw[0][4]);
    ll fabu_stat = get_stat(sw[1][0], sw[1][1], sw[1][2], sw[1][3], sw[1][4]);
    ll cri_after_stat = get_stat(sw[0][0] - sw[2][0] + sw[3][0], sw[0][1] - sw[2][1] + sw[3][1], sw[0][2] - sw[2][2] + sw[3][2], sw[0][3] - sw[2][3] + sw[3][3], sw[0][4] - sw[2][4] + sw[3][4]);
    ll fabu_after_stat = get_stat(sw[1][0] + sw[2][0] - sw[3][0], sw[1][1] + sw[2][1] - sw[3][1], sw[1][2] + sw[2][2] - sw[3][2], sw[1][3] + sw[2][3] - sw[3][3], sw[1][4] + sw[2][4] - sw[3][4]);

    if(cri_after_stat > cri_stat) {
        cout << "+\n";
    }
    else if(cri_after_stat == cri_stat) {
        cout << "0\n";
    }
    else {
        cout << "-\n";
    }
    
    if(fabu_after_stat > fabu_stat) {
        cout << "+\n";
    }
    else if(fabu_after_stat == fabu_stat) {
        cout << "0\n";
    }
    else {
        cout << "-\n";
    }

    return 0;
}