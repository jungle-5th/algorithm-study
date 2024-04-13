//// BOJ 1715

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N;
priority_queue<int, vector<int>, greater<int>> card;

int main() {
    cin >> N;
    if(N == 1) {
        cout << 0;
        return 0;
    }
    for(int i = 0; i < N; i++) {
        int temp;
        cin >> temp;
        card.push(temp);
    }
    int total = 0;
    while(!card.empty()) {
        int A = card.top();
        card.pop();
        if(card.empty()) {
            total += A;
            break;
        }
        int B = card.top();
        card.pop();
        int C = A + B;
        total += C;
        if(card.empty()) {
            break;
        }
        card.push(C);
    }
    cout << total;

    return 0;
}
