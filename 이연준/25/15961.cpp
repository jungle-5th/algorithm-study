/// BOJ 15961 회전 초밥

#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n, d, k, c;
vector<int> sushi;
int MAX = 0;

int main() {
    cin >> n >> d >> k >> c;
    vector<int> eat(d + 1, 0);
    for(int i = 0; i < n; i++) {
        int s;  cin >> s;
        sushi.push_back(s);
    }
    eat[c]++;
    int combo = 1;
    for(int i = 0; i < k; i++) {
        if(!eat[sushi[i]]) {
            combo++;
        }
        eat[sushi[i]]++;
    }
    MAX = max(MAX, combo);
    int lp = 0, rp = k - 1;
    while(lp <= n - 1) {
        eat[sushi[lp]]--;
        if(!eat[sushi[lp]]) {
            combo--;
        }
        lp++;
        rp++;
        if(rp >= n) rp -= n;
        if(!eat[sushi[rp]]) {
            combo++;
            MAX = max(MAX, combo);
            if(MAX == d) {
                cout << MAX;
                return 0;
            }
            if(MAX == k + 1) {
                cout << MAX;
                return 0;
            }
        }
        eat[sushi[rp]]++;
    }
    cout << MAX;

    return 0;
}