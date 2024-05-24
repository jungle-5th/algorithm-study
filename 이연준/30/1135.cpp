/// BOJ 1135 뉴스 전하기

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> parent;
vector<int> child[50];

int dfs(int node) {
    if(child[node].size() == 0) {
        return 0;
    }
    vector<int> time;
    for(int i = 0; i < child[node].size(); i++) {
        time.push_back(dfs(child[node][i]));
    }
    sort(time.begin(), time.end(), greater<int>());
    for(int i = 0; i < time.size(); i++) {
        time[i] += i + 1;
    }
    return *max_element(time.begin(), time.end());
}

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        Time[i] = 0;
        int boss;  cin >> boss;
        parent.push_back(boss);
        if(i > 0) {
            child[boss].push_back(i);
        }
    }
    cout << dfs(0);

    return 0;
}