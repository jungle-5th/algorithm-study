/// BOJ 13975 파일 합치기 3

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int T;  cin >> T;
    while(T--) {
        int K;  cin >> K;
        priority_queue<int, vector<int>, greater<int>> pq;
        for(int i = 0; i < K; i++) {
            int page;   cin >> page;
            pq.push(page);
        }
        int ans = 0;
        while(pq.size() >= 2) {
            int a = pq.top();
            pq.pop();
            int b = pq.top();
            pq.pop();
            ans += a + b;
            pq.push(a + b);
        }
        cout << ans << "\n";
    }

    return 0;
}