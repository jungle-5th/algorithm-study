/// BOJ 2343 기타 레슨
/// TIL 적어야함
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int N, M;
vector<int> lect;

int main() {
    cin >> N >> M;
    for(int i = 0; i < N; i++) {
        int tmp;    cin >> tmp;
        lect.push_back(tmp);
    }

    int r = accumulate(lect.begin(), lect.end(), 0);        // 블루레이의 최대 길이 : 모든 강의의 길이의 합
    int l = *max_element(lect.begin(), lect.end());         // 블루레이의 최소 길이 : 가장 긴 강의의 길이(그래야 블루레이 하나에 강의 하나 온전히 담을 수 있음)

    while(l <= r) {
        int mid = (l + r) / 2;                              // 블루레이 길이 기준
        int cnt = 0, sum = 0;                               // cnt(블루레이 개수)가 매개 변수가 됨
        for(int i = 0; i < N; i++) {
            if(sum + lect[i] > mid) {                       // 지금까지 담은 강의 + 다음 강의 > mid 면 이번 블루레이 끝
                cnt++;
                sum = 0;
            }
            sum += lect[i];
        }
        if(sum != 0)    cnt++;

        if(cnt > M) {                                       // 총 블루레이 개수가 M개 보다 많으면 블루레이 길이를 늘려야함
            l = mid + 1;
        }
        else {                                              // 총 블루레이 개수가 M개 보다 적으면 블루레이 길이를 줄여야함(mid의 최소값을 원하므로 같아도 더 줄일 수 있는지 확인함)
            r = mid - 1;
        }
    }
    cout << l;

    return 0;
}