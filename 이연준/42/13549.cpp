/// BOJ 13549 숨바꼭질 3

#include <iostream>
#include <vector>
#include <queue>
#define INF 1e9

using namespace std;

int N, K;
vector<pair<int, int>> edge[200000];
vector<int> dist(200000, INF);

void dijkstra(int start) {
    dist[start] = 0;
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});

    while(!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;

        pq.pop();

        for(int i = 0; i < edge[cur].size(); i++) {
            int next = edge[cur][i].first;
            int ncost = edge[cur][i].second;

            if(dist[next] > cost + ncost) {
                dist[next] = cost + ncost;
                pq.push({-dist[next], next});
            }
        }
    }
}

int main() {
    cin >> N >> K;
    if(N >= K) {
        cout << N - K;
        return 0;
    }

    for(int i = 0; i < 2 * K; i++) {
        if(i - 1 >= 0) {
            edge[i].push_back({i - 1, 1});
        }
        if(i + 1 <= 2 * K) {
            edge[i].push_back({i + 1, 1});
        }
        if(i * 2 <= 2 * K) {
            edge[i].push_back({2 * i, 0});
        }
    }
    dijkstra(N);
    cout << dist[K];

    return 0;
}