/// BOJ 17503 맥주 축제

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, K;
vector<pair<long long, long long>> beer;

bool cmp(pair<long long, long long> &a, pair<long long, long long> &b) {
    return a.second < b.second;
}

long long bsearch(long long l, long long r) {
    long long ans = 1e13;
    while(l <= r) {
        long long mid = (l + r) / 2;
        vector<long long> drink;
        for(int i = 0; i < K; i++) {
            if(beer[i].second > mid)    break;      // 오름차순 정렬이라 이후 나오는 것들의 도수는 mid보다 높음
            drink.push_back(beer[i].first);
        }
        if(drink.size() < N) {                      // 마실 수 있는 맥주의 개수가 N보다 적음
            l = mid + 1;
            continue;
        }
        long long sat = 0;
        sort(drink.begin(), drink.end(), greater<long long>());
        for(int i = 0; i < N; i++) {
            sat += drink[i];
        }
        if(sat < M) {
            l = mid + 1;
        }
        else {
            ans = min(ans, mid);
            r = mid - 1;
        }
    }
    return ans;
}

int main() {
    cin >> N >> M >> K;
    for(int i = 0; i < K; i++) {
        int v, c;   cin >> v >> c;
        beer.push_back({v, c});                             // 선호도, 도수
    }   
    sort(beer.begin(), beer.end(), cmp);
    long long dosu = bsearch(beer[0].second, beer[K - 1].second);
    cout << (dosu == 1e13 ? -1 : dosu);
    return 0;
}