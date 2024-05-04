/// BOJ 25187 고인물이 싫어요

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, Q;
vector<int> water(100001);
vector<int> par(100001);

int findP(int node) {
    if(par[node] == node)   return node;
    else    return par[node] = findP(par[node]);
}

void Union(int x, int y) {
    int px = findP(x);
    int py = findP(y);
    if(px == py) {
        return;
    }
    else if(par[px] < par[py]) {
        water[px] += water[py];
        par[py] = px;
    }
    else {
        water[py] += water[px];
        par[px] = py;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M >> Q;
    for(int i = 1; i <= N; i++) {
        cin >> water[i];            // 청정수 : 1, 고인물 : 0
        par[i] = i;
        if(water[i] == 0)   water[i] = -1;
    }
    for(int i = 0; i < M; i++) {
        int u, v;   cin >> u >> v;
        Union(u, v);
    }
    for(int i = 0; i < Q; i++) {
        int visit;  cin >> visit;
        int P = findP(visit);
        if(water[P] > 0)  cout << "1\n";
        else    cout << "0\n";
    }

    return 0;
}