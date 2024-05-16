/// BOJ 14650 걷다보니 신천역 삼 (Small)

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;
vector<int> sam;
vector<int> num = {0, 1, 2};
int ans = 0;

int make_num(vector<int> sam) {
    int ret = 0;
    int n = sam.size();
    for(int i = 0; i < n; i++) {
        ret += sam[i] * pow(10, n - i - 1);
    }
    return ret;
}

void backtrack(int dig) {
    if(dig == N) {
        int res = make_num(sam);
        if(res % 3 == 0) {
            ans++;
            return;
        }
        else {
            return;
        }
    }

    for(int i = 0; i < 3; i++) {
        sam.push_back(num[i]);
        backtrack(dig + 1);
        sam.pop_back(num[i]);
    }
}

int main() {
    cin >> N;
    for(int i = 0; i < 2; i++) {
        sam.push_back(num[i]);
        backtrack(1);
        sam.pop_back(num[i]);
    }

    return 0;
}