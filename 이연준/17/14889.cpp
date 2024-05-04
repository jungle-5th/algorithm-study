/// BOJ 14889 스타트와 링크

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<vector<int>> stat;

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        vector<int> tmp;
        for(int j = 0; j < N; j++) {
            int a;  cin >> a;
            tmp.push_back(a);
        }
        stat.push_back(tmp);
    }
    vector<int> team(N, 0);             // index번 사람이 1팀인지, 2팀인지
    

    return 0;
}