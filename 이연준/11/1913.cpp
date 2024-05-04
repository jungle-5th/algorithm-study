#include <iostream>
#include <vector>

using namespace std;

int Dir_X[4] = {-1, 0, 1, 0};
int Dir_Y[4] = {0, 1, 0, -1};

int main() {
    int N;  cin >> N;
    vector<vector<int>> snail(N, vector<int>(N, 0));
    int target; cin >> target;

    int mid = N / 2;
    int x = mid, y = mid;
    int dir = 0;
    int move = 1;
    int num = 1;
    int ansx, ansy;

    int final3 = 0;
    int twice = 0;
    int k = 1;
    while(move < N) {
        int push = move;
        if(move == N - 1) {
            if(final3 == 3) {               // 마지막에 3번 움직이면 끝
                break;
            }
            final3++;
        }
        else {
            if(twice == 2) {
                move++;
                twice = 0;
                continue;
            }
            twice++;
        }
        while(push--) {
            if(num == target) {
                ansx = x + 1, ansy = y + 1;
            }
            snail[x][y] = num;
            num++;
            x += Dir_X[dir];
            y += Dir_Y[dir];
        }
        dir++;
        dir %= 4;
    }
    snail[x][y] = num;
    if(num == target) {
        ansx = x + 1;
        ansy = y + 1;
    }
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            cout << snail[i][j] << " ";
        }
        cout << endl;
    }
    cout << ansx << " " << ansy;

    return 0;
}