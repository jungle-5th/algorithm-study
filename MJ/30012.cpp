// https://www.acmicpc.net/problem/30012
// 개구리 매칭

#include <iostream>

using namespace std;

int main() {


int juho;
int n_of_frogs;
cin >> juho >> n_of_frogs;

// dist[i]는 i번 개구리와 주호 사이의 거리
int dist[(n_of_frogs + 1)];
for (int i = 1; i <= n_of_frogs; i++) {
    int cord;
    cin >> cord;
    if (cord > juho) dist[i] = cord-juho;
    else dist[i] = juho-cord;
}

int k_of_leap;
int l_of_walk;
cin >> k_of_leap >> l_of_walk;

int min_cost = 2147483647;
int min_frog;
for (int j = 1; j <= n_of_frogs; j++) {
    int cost;
    if (dist[j] < 2*k_of_leap) cost = 2*k_of_leap - dist[j];
    else cost = (dist[j] - 2*k_of_leap) * l_of_walk;

    if (cost < min_cost) {
        min_cost = cost;
        min_frog = j;
    }
}
// cout << "leap " << k_of_leap << "  walk " << l_of_walk << "  minfrog is at " << dist[min_frog] <<endl; 
cout << min_cost << " " << min_frog;

}