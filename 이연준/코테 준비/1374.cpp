/// BOJ 1374 강의실

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N;

bool cmp(vector<int> &a, vector<int> &b) {
    if(a[1] == b[1]) {
        return a[2] < b[2];
    }
    else
        return a[1] < b[1];
}

int main() {
    cin >> N;
    vector<vector<int>> info(N, vector<int>(3));
    for(int i = 0; i < N; i++) {
        cin >> info[i][0] >> info[i][1] >> info[i][2];
    }
    sort(info.begin(), info.end(), cmp);
    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(info[0][2]);
    int ans = 1;
    for(int i = 1; i < N; i++) {
        if(pq.top() > info[i][1]) {
            pq.push(info[i][2]);
        }
        else {
            pq.pop();
            pq.push(info[i][2]);
        }
        ans = max(ans, (int)pq.size());
    }
    cout << ans;

    return 0;
}