/// BOJ 16398 행성 연결

#include <iostream>
#include <vector>
#include <queue>
#define INF 999999999

using namespace std;

int N;
long long answer = 0;
vector<pair<int, int>> edge[1001];
vector<bool> visited(1001, false);

void prim() {
    priority_queue<pair<int, int>> pq;
    for(int i = 0; i < edge[1].size(); i++) {
        int next = edge[1][i].first;
        int cost = edge[1][i].second;

        pq.push({-cost, next});
    }
    visited[1] = true;

    while(!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if(visited[cur])   continue;

        visited[cur] = true;
        answer += cost;

        for(int i = 0; i < edge[cur].size(); i++) {
            int next = edge[cur][i].first;
            int ncost = edge[cur][i].second;

            if(visited[next])   continue;

            pq.push({-ncost, next});
        }
    }
}

int main() {
    cin >> N;
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            int d;  cin >> d;
            if(d == 0)  continue;

            edge[i].push_back({j, d});
        }
    }
    prim();
    cout << answer;
    return 0;
}