/// BOJ 27313 효율적인 애니메이션 감상

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, K;
vector<int> anime;

int main() {
    cin >> N >> M >> K;
    for(int i = 0; i < N; i++) {
        int t;   cin >> t;
        if(t > M)    continue;           // M 보다 긴 시간의 애니는 못보니까 안 넣음
        anime.push_back(t);
    }
    sort(anime.begin(), anime.end());       // 오름차순 정렬
    vector<int> check;
    for(int i = 0; i < anime.size(); i++) {
        int t;
        if(i < K) {
            t = anime[i];                   // 한 그룹 안에만 들어갈 수 있는 애니메이션이므로 애니메이션 보는데 걸리는 시간 = anime[i] 
        }
        else {
            t = check[i - K] + anime[i];    // 한 그룹 안에 들어갈 수 없는 수이고, 애니메이션 보는데 걸리는 시간을 최소화해야 하므로
                                            // 현재부터 K개 전까지 한 그룹, 그 이전에 있는 것을 한 그룹으로 생각
        }

        if(t <= M) {
            check.push_back(t);             // 현재 애니메이션까지 봤을 때 걸리는 시간의 최소 합이 M보다 작거나 같으면 개수 하나 추가
        }
        else {
            break;                          // M보다 크면 바로 끝
        }
    }
    cout << check.size();

    return 0;
}