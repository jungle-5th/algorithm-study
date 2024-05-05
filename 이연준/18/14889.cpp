/// BOJ 14889 스타트와 링크

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N;
int MIN = 99999999;
vector<vector<int>> stat;
vector<bool> visited;
vector<int> all;

vector<int> left(vector<int> team) {
    vector<int> team2 = all;
    for(int i = 0; i < team.size(); i++) {
        team2.erase(remove(team2.begin(), team2.end(), team[i]), team2.end());
    }
    return team2;
}

void backtrack(vector<int> team, int start, int person) {
    team.emplace_back(person);
    if(team.size() == N / 2) {
        vector<int> team2 = left(team);
        int stat1 = 0, stat2 = 0;
        for(int i = 0; i < N / 2; i++) {
            for(int j = 0; j < N / 2; j++) {
                stat1 += stat[team[i]][team[j]];
                stat2 += stat[team2[i]][team2[j]];
            }
        }
        MIN = min(MIN, abs(stat1 - stat2));
        return;        
    }

    for(int i = start + 1; i < N; i++) {
        if(visited[i])  continue;

        visited[i] = true;
        backtrack(team, i, i);
        visited[i] = false;
    }
}


int main() {
    cin >> N;
    visited.resize(N);
    all.resize(N);
    for(int i = 0; i < N; i++) {
        vector<int> tmp;
        for(int j = 0; j < N; j++) {
            int a;  cin >> a;
            tmp.push_back(a);
        }
        stat.push_back(tmp);
        visited[i] = false;
        all[i] = i;
    }
    for(int i = 0; i < N; i++) {
        visited[i] = true;
        backtrack({}, i, i);
        visited[i] = false;
    }
    cout << MIN;

    return 0;
}