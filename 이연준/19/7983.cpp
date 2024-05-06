/// BOJ 7983 내일 할거야

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<pair<int, int>> task;

bool cmp(pair<int, int> &a, pair<int, int> &b) {
    if(a.first == b.first)  return a.second > b.second;
    return a.first > b.first;
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        int d,t;    cin >> d >> t;
        task.push_back({t, d});           // 마감일, 걸리는 일
    }
    sort(task.begin(), task.end(), cmp); // 마감일 기준 정렬
    int day = task[0].first;                // 과제를 마감하기 위해서 시작해야되는 날짜
    for(int i = 0; i < n; i++) {
        if(task[i].second < day)    day = task[i].second;           // 마감일이 시작일 보다 이른 경우(tast[i].second : i번째 과제의 마감일, day : 과제 시작일)
        day -= tast[i].first;                                       // 과제를 시작해야되는 날짜를 구하기 위해 걸리는 시간 빼줌
    }
    if(day) cout << day;
    else    cout << 0;

    return 0;
}