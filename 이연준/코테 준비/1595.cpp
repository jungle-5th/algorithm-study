/// 1595 북쪽나라의 도로

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define INF 1e9

using namespace std;

vector<pair<int, int>> edge[10001];
vector<int> dist1(10001, INF);
vector<int> dist2(10001, INF);

void dijkstra(int node) {
    priority_queue<pair<int, int>> pq;
    pq.push({0, node});
    dist1[node] = 0;

    while(!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        for(int i = 0; i < edge[cur].size(); i++) {
            int next = edge[cur][i].first;
            int ncost = edge[cur][i].second;

            if(dist1[next] > dist1[cur] + ncost) {
                dist1[next] = dist1[cur] + ncost;
                pq.push({-dist1[next], next});
            }
        }
    }
}

void dijkstra2(int node) {
    priority_queue<pair<int, int>> pq;
    pq.push({0, node});
    dist2[node] = 0;

    while(!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        for(int i = 0; i < edge[cur].size(); i++) {
            int next = edge[cur][i].first;
            int ncost = edge[cur][i].second;

            if(dist2[next] > dist2[cur] + ncost) {
                dist2[next] = dist2[cur] + ncost;
                pq.push({-dist2[next], next});
            }
        }
    }
}

int main() {
    int maxidx = 0;
    while(!cin.eof()) {
        int a, b, c;
        cin >> a >> b >> c;
        edge[a].push_back({b, c});
        edge[b].push_back({a, c});
        maxidx = max(maxidx, max(a, b));
    }
    dijkstra(1);
    int idx = max_element(dist1.begin() + 1, dist1.begin() + maxidx + 1) - dist1.begin();
    dijkstra2(idx);
    cout << *max_element(dist2.begin() + 1, dist2.begin() + maxidx + 1);
    return 0;
}