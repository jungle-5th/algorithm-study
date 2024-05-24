/// BOJ 18429 근손실

#include <iostream>
#include <vector>

using namespace std;

int N, K;
vector<int> work;
vector<bool> visited;
int cnt = 0;

void backtrack(int ex, int total, int num) {
    int next = total + work[ex] - K;
    if(next < 0) {
        return;
    }
    if(num == N) {
        cnt++;
        return;
    }

    for(int i = 0; i < N; i++) {
        if(visited[i])   continue;

        visited[i] = true;
        backtrack(i, next, num + 1);
        visited[i] = false;
    }
}

int main() {
    cin >> N >> K;
    work.resize(N);
    visited.resize(N);
    for(int i = 0; i < N; i++) {
        cin >> work[i];
        visited[i] = false;
    }
    for(int i = 0; i < N; i++) {
        visited[i] = true;
        backtrack(i, 0, 1);
        visited[i] = false;
    }
    cout << cnt;

    return 0;
}