/// BOJ 26085 효구와 호규(Easy)

#include <iostream>
#include <vector>

using namespace std;

int N, M;
int zero = 0, one = 0;
vector<vector<int>> card;

int main() {
    cin >> N >> M;
    card.resize(N);
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            int tmp;    cin >> tmp;
            if(tmp == 0)    zero++;
            else    one++;

            card[i].push_back(tmp);
        }
    }
    if(N * M % 2 || one % 2 || zero % 2) {
        cout << -1;
        return 0;
    }

    bool flag = false;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M - 1; j++) {
            if(!(card[i][j] ^ card[i][j + 1])) {
                flag = true;
                break;
            }
            if(i > 0) {
                if(!(card[i - 1][j] ^ card[i][j])) {
                    flag = true;
                    break;
                }
            }
        }
        if(flag)    break;
    }
    if(flag)    cout << 1;
    else    cout << - 1;

    return 0;
}