/// BOJ 27313 효율적인 애니메이션 감상

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, K;
vector<int> anime;

int find_two_pointer(int lp, int rp) {
    while(anime[rp] > M) {
        rp--;
        if(rp == lp) {
            break;
        }
    }
    return rp;
}

int main() {
    cin >> N >> M >> K;
    anime.resize(N);
    for(int i = 0; i < N; i++) {
        cin >> anime[i];
    }
    sort(anime.begin(), anime.end(), greater<int>());           // 내림차순으로 정렬하긴 했지만 오름차순으로 했을 때가 정답일 때도 있음
    int ans1 = 0;
    int idx1 = 0;
    int M2 = M;
    // 큰거부터 탐색
    while(1) {
        while(idx1 < N && anime[idx1] > M) {
            idx1++;
        }
        if(idx1 >= N) {
            break;
        }
        if(idx1 + K >= N) {
            ans += N - idx1;
            M -= anime[idx1];
            idx1 = N;

        }
        else {
            ans += K;
            M -= anime[idx1];
            idx1 += K;
        }
        if(M == 0) {
            break;
        }
    }

    // 작은거부터 탐색
    int ans2 = 0;
    int idx2 = -1;
    int l = idx2;
    reverse(anime.begin(), anime.end());
    while(1) {
        l = idx2;
        if(idx2 + K < N) {
            idx2 += K;
        }
        else {
            idx2 = N - 1;
        }
        while(anime[idx2] > M) {
            idx2--;
            if(idx2 <= l) {
                break;
            }
        }
        if(idx2 > l) {
            ans2 += idx2 - l;
            M2 -= anime[idx2];
        }
        else {
            break;
        }
        if(M2 < anime[idx2 + 1]) {
            break;
        }
        if(idx2 == N - 1) {
            break;
        }
    }
    cout << max(ans1, ans2);

    return 0;
}