/// BOJ 20115 에너지 드링크

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<double> drink;
int N;

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        double energy;  cin >> energy;
        drink.emplace_back(energy);
    }
    sort(drink.begin(), drink.end());
    double total = 0;
    for(int i = 0; i < N - 1; i++) {
        total += drink[i];
    }
    
    cout << total / 2 + drink[N - 1];

    return 0;
}