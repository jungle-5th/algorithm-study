/// BOJ 18126 너구리 구구

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, long long>> edge[5001];
vector<bool> visited(5001, false);

long long dfs(int node) {
    long long depth = 0;
    visited[node] = true;
    long long origin = depth;
    for(int i = 0; i < edge[node].size(); i++) {
        if(visited[edge[node][i].first])    continue;
        depth = max(depth, origin + edge[node][i].second + dfs(edge[node][i].first));
    }
    return depth;
}

int main() {
    cin >> N;
    for(int i = 0; i < N - 1; i++) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        edge[a].push_back({b, c});
        edge[b].push_back({a, c});
    }
    long long ans = dfs(1);
    cout << ans;
    
    return 0;
}