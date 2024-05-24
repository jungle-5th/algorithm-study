/// BOJ 1516 게임 개발

#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;
map<int, vector<int>> build;
vector<int> Time;

int N;

int main() {
    cin >> N;
    Time.resize(N + 1);
    vector<int> indegree(N + 1, 0);
    vector<int> answer(N + 1, 0);
    for(int i = 1; i <= N; i++) {
        cin >> Time[i];
        int b = 0;
        cin >> b;
        while(b != -1) {
            build[b].push_back(i);
            indegree[i]++;
            cin >> b;
        }
    }
    
    queue<int> q;
    for(int i = 1; i <= N; i++) {
        if(indegree[i] == 0) {
            q.push(i);
        }
    }
    for(int i = 0; i < N; i++) {
        if(q.empty())   break;
        
        int from = q.front();
        q.pop();
        answer[from] += Time[from];
        
        for(int i = 0; i < build[from].size(); i++) {
            int next = build[from][i];
            indegree[next]--;

            if(answer[next] > 0)    answer[next] = max(answer[next], answer[from]);
            else                    answer[next] = answer[from];

            if(indegree[next] == 0) {
                q.push(next);
            }
        }
    }
    for(int i = 1; i <= N; i++) {
        cout << answer[i] << "\n";
    }

    return 0;
}