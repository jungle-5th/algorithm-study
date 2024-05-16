/// BOJ 1967 트리의 지름

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define INF 1e9

using namespace std;

int n;
vector<pair<int, int>> edge[10001];

void dijkstra(int node, vector<int> &dist) {
    priority_queue<pair<int, int>> pq;
    pq.push({0, node});
    dist[node] = 0;
    while(!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        
        pq.pop();

        for(int i = 0; i < edge[cur].size(); i++) {
            int next = edge[cur][i].first;
            int nCost = cost + edge[cur][i].second;

            if(nCost < dist[next]) {
                dist[next] = nCost;
                pq.push({-nCost, next});
            }
        }
    }
}

int main() {
    cin >> n;
    vector<int> dist1(n + 1, INF);
    vector<int> dist2(n + 1, INF);
    while(!cin.eof()) {
        int p, c, w;
        cin >> p >> c >> w;
        edge[p].push_back({c, w});
        edge[c].push_back({p, w});

    }
    dijkstra(1, dist1);
    dist1.erase(dist1.begin());
    int Midx = max_element(dist1.begin(), dist1.end()) - dist1.begin() + 1;
    dijkstra(Midx, dist2);
    dist2.erase(dist2.begin());
    cout << *max_element(dist2.begin(), dist2.end());

    return 0;
}