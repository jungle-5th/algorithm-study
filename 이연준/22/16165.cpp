/// BOJ 16165 걸그룹 마스터 준석이

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int N, M;

int main() {
    cin >> N >> M;
    map<string, vector<string>> GtoM;
    map<string, string> MtoG;
    for(int i = 0; i < N; i++) {
        string group;   cin >> group;
        GtoM[group] = {};
        int mem;    cin >> mem;
        for(int j = 0; j < mem; j++) {
            string member;  cin >> member;
            GtoM[group].push_back(member);
            MtoG[member] = group;
        }
    }
    for(auto iter = GtoM.begin(); iter != GtoM.end(); iter++) {
        sort(GtoM[iter->first].begin(), GtoM[iter->first].end());
    }
    while(M--) {
        string prob;    cin >> prob;
        int cat;    cin >> cat;
        if(cat) {
            cout << MtoG[prob] << "\n";
        }
        else {
            for(auto mem : GtoM[prob]) {
                cout << mem << "\n";
            }
        }
    }

    return 0;
}