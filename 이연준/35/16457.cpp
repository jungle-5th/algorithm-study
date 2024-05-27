/// BOJ 16457 단풍잎 이야기

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, k;
vector<bool> skill(21, false);
vector<vector<int>> quest(100, vector<int>(10));
int MAX = 0;

void check() {
    int tot = 0;
    for(int i = 0; i < m; i++) {
        bool flag = true;
        for(int j = 0; j < k; j++) {
            if(!skill[quest[i][j]]) {
                flag = false;
                break;
            }
        }
        if(flag) {
            tot++;
        }
        else {
            continue;
        }
    }
    MAX = max(MAX, tot);
}

void backtrack(int idx, int cnt) {
    if(cnt == n) {
        check();
        return;
    }
    for(int i = idx + 1; i <= 2 * n; i++) {
        skill[i] = true;
        backtrack(i, cnt + 1);
        skill[i] = false;
    }
}

int main() {
    cin >> n >> m >> k;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < k; j++) {
            cin >> quest[i][j];
        }
    }
    for(int i = 1; i <= 2 * n - k + 1; i++) {
        skill[i] = true;
        backtrack(i, 1);
        skill[i] = false;
    }
    cout << MAX;

    return 0;
}