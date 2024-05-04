/// BOJ 24460 특별상이라도 받고 싶어

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;

int recursive(vector<vector<int>> table) {
    int sz = table.size();
    if(sz == 2) {
        vector<int> srt(4);
        for(int i = 0; i < 4; i++) {
            srt[i] = table[i / 2][i % 2];
        }
        sort(srt.begin(), srt.end());

        return srt[1];
    }
    vector<vector<int>> qvec1(sz / 2, vector<int>(sz / 2));
    vector<vector<int>> qvec2(sz / 2, vector<int>(sz / 2));
    vector<vector<int>> qvec3(sz / 2, vector<int>(sz / 2));
    vector<vector<int>> qvec4(sz / 2, vector<int>(sz / 2));
    for(int i = 0; i < sz / 2; i++) {
        for(int j = 0; j < sz / 2; j++) {
            qvec1[i][j] = table[i][j];
            qvec2[i][j] = table[i][j + sz / 2];
            qvec3[i][j] = table[i + sz / 2][j];
            qvec4[i][j] = table[i + sz / 2][j + sz / 2];
        }
    }
    vector<vector<int>> ret(2, vector<int>(2));
    ret[0][0] = recursive(qvec1);
    ret[0][1] = recursive(qvec2);
    ret[1][0] = recursive(qvec3);
    ret[1][1] = recursive(qvec4);

    vector<int> srt(4);
    for(int i = 0; i < 4; i++) {
        srt[i] = ret[i / 2][i % 2];
    }
    sort(srt.begin(), srt.end());

    return srt[1];
}

int main() {
    cin >> N;
    vector<vector<int>> table;
    if(N != 1) {
        for(int i = 0; i < N; i++) {
            vector<int> tmp;
            for(int j = 0; j < N; j++) {
                int t;  cin >> t;
                tmp.push_back(t);
            }
            table.push_back(tmp);
        }
    }
    else {
        int tmp;
        cin >> tmp;
        cout << tmp;
        return 0;
    }

    int res = recursive(table);
    cout << res;

    return 0;
}