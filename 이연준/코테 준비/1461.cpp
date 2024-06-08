/// BOJ 1461 도서관

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> plus;
    vector<int> minus;
    for(int i = 0; i < N; i++) {
        int book;
        cin >> book;
        if(book > 0) {
            plus.push_back(book);       // 양수에 위치한 책과
        }
        else {
            minus.push_back(-book);     // 음수에 위치한 책을 따로 저장함
        }
    }
    sort(plus.begin(), plus.end());
    sort(minus.begin(), minus.end());
    int answer =0;
    int bigger = 0;
    int pm, mm;
    if(plus.size() && minus.size()) {       // 만약 양 쪽 다 책이 존재한다면
        pm = plus[plus.size() - 1];
        mm = minus[minus.size() - 1];
        if(pm > mm) {
            bigger = 1;                     // 어느 쪽이 더 큰지 표시
        }
        else {
            bigger = -1;
        }
    }
    else if(plus.size()) {                  // 한 쪽에만 존재하면
        pm = plus[plus.size() - 1];         // 어느 쪽이 존재하는지 저장
        bigger = 1;
    }
    else {
        mm = minus[minus.size() - 1];
        bigger = -1;
    }
    for(int i = plus.size() - 1; i >= 0; i -= M) {          // 절대값이 큰 값부터 왕복 시작
        answer += plus[i] * 2;
    }
    for(int i = minus.size() - 1; i >= 0; i -= M) {
        answer += minus[i] * 2;
    }
    if(bigger > 0) {        // 순회 끝난 후 가장 절대값이 큰 값을 한 번 빼줌(마지막은 왕복하지 않고 책 갖다놓고 끝)
        answer -= pm;
    }
    else {
        answer -= mm;
    }
    cout << answer;

    return 0;
}