/// BOJ 2531 회전 초밥

#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n, d, k, c;
vector<int> sushi;
int MAX = 0;

int main() {
    cin >> n >> d >> k >> c;
    for(int i = 0; i < n; i++) {
        int s;  cin >> s;
        sushi.push_back(s);
    }
    map<int, int> eat;
    for(int i = 0; i < k; i++) {
        if(eat.find(sushi[i]) == eat.end()) {
            eat[sushi[i]] = 1;
        }
        else {
            eat[sushi[i]]++;
        }
    }
    int lp = 0, rp = k - 1;
    while(lp <= n - 1) {
        if(eat.size() >= MAX) {
            if(eat.find(c) != eat.end()) {
                MAX = eat.size();
            }
            else {
                MAX = eat.size() + 1;
            }
        }
        if(eat[sushi[lp]] == 1) {
            eat.erase(sushi[lp]);
        }
        else {
            eat[sushi[lp]]--;
        }
        lp++;
        rp++;
        if(rp >= n) rp -= n;
        if(eat.find(sushi[rp]) == eat.end()) {
            eat[sushi[rp]] = 1;
        }
        else {
            eat[sushi[rp]]++;
        }
    }
    cout << MAX;

    return 0;
}