//// BOJ 22866 탑 보기
//// TIL 기록 필요
#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#define INF 99999999

using namespace std;

int N;
vector<int> building(100000);

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> building[i];
    }
    vector<int> highNum(N, 0);
    vector<vector<int>> neareast(N, vector<int>(2, INF));
    stack<pair<int, int>> right;        // 건물 높이, 건물 인덱스
    right.push({building[0], 0});
    for(int i = 1; i < N; i++) {        // i 번째 건물 기준 왼쪽으로 볼 수 있는지 확인
        while(!right.empty() && right.top().first <= building[i]) {         // 만약 stack top 보다 현재 건물이 낮다면 볼 수 없는 건물이므로 pop, stack이 empty가 되면 while문 탈출
            right.pop();                                                    // pop하면 stack top부터 오름차순으로 건물이 들어가있음
        }
        if(!right.empty()) {
            neareast[i][0] = right.top().second;                            // stack이 비어있지 않으면 stack의 탑이 왼쪽으로 볼 수 있는 건물 중에 가장 가까운 건물
        }
        highNum[i] += right.size();                                         // stack에 남아있는 개수가 왼쪽으로 볼 수 있는 건물의 개수
        right.push({building[i], i});                                       // 현재 건물의 높이와 인덱스 push
    }
    stack<pair<int, int>> left;        // 건물 높이, 건물 인덱스
    left.push({building[N - 1], N - 1});
    for(int i = N - 2; i >= 0; i--) {                                       // 위와 동일하고 방향만 반대
        while(!left.empty() && left.top().first <= building[i]) {
            left.pop();
        }
        if(!left.empty()) {
            neareast[i][1] = left.top().second;
        }
        highNum[i] += left.size();
        left.push({building[i], i});
    }
    for(int i = 0; i < N; i++) {
        if(highNum[i] > 0) {
            cout << highNum[i] << " ";
            if(abs(i - neareast[i][0]) == abs(i - neareast[i][1]) || abs(i - neareast[i][0]) < abs(i - neareast[i][1])) {
                cout << neareast[i][0] + 1;
            }
            else{
                cout << neareast[i][1] + 1;
            }
        }
        else{
            cout << highNum[i];
        }
        cout << "\n";
    }

    return 0;
}