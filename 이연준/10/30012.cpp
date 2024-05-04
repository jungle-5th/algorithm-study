/// BOJ 30012 개구리 매칭

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int S, N, K, L;
vector<int> E;

int main() {
    cin >> S >> N;
    for(int i = 0; i < N; i++) {
        int tmp;    cin >> tmp;
        E.push_back(tmp);
    }
    cin >> K >> L;

    int ansHP = 9999999;
    int ansidx = -1;

    for(int i = 0; i < N; i++) {
        int dist = abs(S - E[i]);
        int deltaHP = 0;
        if(dist > 2 * K) {
            deltaHP = dist - (2 * K) + L * (dist - 2 * K);
        }
        else {
            deltaHP = 2 * K - dist;
        }
        if(ansHP < deltaHP) continue;

        ansHP = deltaHP;
        ansidx = i;
    }

    cout << ansHP << " " << ansidx + 1;

    return 0;
}