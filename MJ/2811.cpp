// https://www.acmicpc.net/problem/2811
// 상범이의 우울

// 문제
// 민균이와 상범이는 오래된 연인이다.
// 요즘따라 냉랭해진 상범이의 태도를 본 민균이는 상범이의 기분을 예측한 다음, 상범이가 우울해지기 전에 꽃을 선물함으로써 그의 기분을 상큼하게 만들어주려고 한다.
// 상범이의 기분은 하루씩 정수로 표현되는데, 기분이 좋은 날은 양수로 표현되고 우울한 날은 음수로 표현된다.
// (따라서 음수만 나타나는 연속적인 구간을 '우울한 기간' 또는 '우울 기간'이라고 한다)
// 한편, 상범이의 우울 기간의 길이가 T일 땐, 구간의 시작으로부터 2T일 전부터 구간의 시작 바로 전날까지 꽃을 선물해야 그의 우울함을 덜어줄 수 있다.
// 주의해야 할 점은 길이가 가장 긴 우울 구간의 경우에는 2T일 이전이 아닌 3T일 이전부터 꽃을 선물해야 한다는 점이다. 현재부터 가장 빠른 상범이의 우울기간을 T_f 라고 하자.
// 만약 현재부터 계속해서 꽃을 선물해도 가장 빠른 상범이의 우울기간까지 2 * T_f 만큼 꽃을 선물할 수 없다고 하더라고 줄 수 있는만큼 꽃을 줘야 한다. (단, 이런 최장 우울 구간이 여러 개인 경우에는 그중 한 구간만 이렇게 하면 되고, 나머지 구간은 2T로 적용하면 된다)
// 민균이가 예측한 앞으로 N일간의 상범이의 기분이 주어졌을 때, 이 N일 중 그가 상범이에게 꽃을 줘야하는 날의 수(사야 하는 꽃의 개수)의 최댓값을 구해보자.

// 입력
// 첫 번째 줄에는 예측한 날의 수 N (1 ≤ N ≤ 100,000)이 주어진다.
// 두 번째 줄에는 상범이의 기분을 나타내는 N개의 정수(|기분| ≤ 100)가 주어진다.

// 출력
// 민균이가 상범이에게 꽃을 주어야하는 날의 최댓값을 출력한다.

// 예제 입력 1 
// 8
// 1 -1 4 3 8 -2 3 -3
// 예제 출력 1 
// 6


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int count_flowers(vector<bool> days) {
    int count = 0;
    for (int i = 0; i < days.size(); i++) {
        if (days[i]) count += 1;
    }
    return count;
}

int main() {
//////////////////////////////////////////////////////
int n_of_days;
cin >> n_of_days;

bool kibun = true;
int start;
int streak = 0;
int max_streak = 0;
vector<pair<int, int>> jogong;
vector<pair<int, int>> extra;
vector<bool> days(n_of_days, false);

for (int i = 0; i < n_of_days; i++) {
    int today;
    cin >> today;
    if (today < 0) {
        if (!kibun) {
            streak += 1;
        }
        else {
            kibun = false;
            streak = 1;
            start = i;
        }
        if (i == n_of_days - 1) jogong.push_back({streak, start});
        if (streak > max_streak) max_streak = streak;

    }
    else {
        if (!kibun) {
            jogong.push_back({streak, start});
            streak = 0;
            kibun = true;
        }
    }
}

for (int n = 0; n < jogong.size(); n++) {
    for (int d = jogong[n].second - 1; 0 <= d && (jogong[n].second-2*jogong[n].first) <= d; d--) {
        days[d] = true;
    }
    if (jogong[n].first == max_streak) {
        if (jogong[n].second-2*jogong[n].first < 0) continue;
        extra.push_back({max_streak, jogong[n].second-2*jogong[n].first});
    }
}

int result = count_flowers(days);
for (int itr = 0; itr < extra.size(); itr++) {
    vector<bool> flowers = days;
    for(int d = extra[itr].second - 1; 0 <= d && (extra[itr].second - max_streak) <= d; d--){
        flowers[d] = true;
    }
    int res = count_flowers(flowers);
    if (res > result) result = res;
}

cout << result;
//////////////////////////////////////////////////////
return 0;}