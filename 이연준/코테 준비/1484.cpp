/// BOJ 1484 다이어트

#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    int G;
    cin >> G;
    int num = 2;
    while(pow(num, 2) - pow(num - 1, 2) < G) {
        num++;
    }
    vector<int> ans;
    int l = 1, r = 2;
    while(r <= num) {
        if(pow(r, 2) - pow(l, 2) < G) {
            r++;
        }
        else if(pow(r, 2) - pow(l, 2) > G) {
            l++;
        }
        else {
            ans.push_back(r);
            r++;
        }
    }
    sort(ans.begin(), ans.end());
    if(ans.size() == 0) {
        cout << -1;
        return 0;
    }
    for(auto a : ans) {
        cout << a << "\n";
    }
    return 0;
}