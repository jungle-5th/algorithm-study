// https://www.acmicpc.net/problem/17503
// 맥주 축제

// 문제
// 내일부터 N일 동안 대구광역시에서 맥주 축제가 열립니다!
// 이 축제에서는 무려 K종류의 맥주를 무료로 제공합니다. 축제 주최자는 축제에서 더 많은 참가자들이 다양한 종류의 맥주를 즐겼으면 합니다.
// 그래서 축제에서 참가자들은 하루에 맥주 1병만 받을 수 있고, 이전에 받았던 종류의 맥주는 다시 받을 수 없습니다.
// 맥주를 정말로 사랑하는 대학생 전씨는 무료 맥주 소식에 신이 났습니다. 전씨는 이 맥주 축제에 참가해 총 N일 동안 맥주 N병을 마시려 합니다.
// 하지만 전씨에게는 큰 고민이 있었습니다. 전씨는 맥주를 사랑하지만, 도수가 높은 맥주를 마시면 기절하는 맥주병이 있습니다.
// 전씨는 맥주를 마시다 기절하면 늦잠을 자 다음 날 1교시 수업에 결석해 F를 받게 될 수도 있습니다.
// 전씨는 고민을 해결하기 위해 천재석사 현씨과 천재박사 승씨에게 자신의 간을 강력하게 만들어달라고 부탁했습니다.
// 하지만 간을 강력하게 만드는 비용이 너무 비싸서, 전씨는 간을 가능한 한 조금만 강화할 계획을 세웠습니다. 우선, K종류의 맥주에 각각 '선호도'와 '도수 레벨'을 매겼습니다.
// 선호도는 전씨가 해당 맥주를 얼마나 좋아하는지를 나타내는 수치이고, 도수 레벨은 해당 맥주의 도수가 얼마나 강한지를 나타내는 수치입니다.
// 편의상 전씨는 선호도와 도수 레벨을 정수로 매겼습니다.
// 만약, 마시는 맥주의 도수 레벨이 전씨의 간 레벨보다 높으면 맥주병이 발병해 기절해버리고 맙니다.
// 또한, 전씨는 맥주병에 걸리지 않으면서도 자신이 좋아하는 맥주를 많이 마시고 싶어합니다. 따라서, 마시는 맥주 N개의 선호도 합이 M이상이 되게 하려 합니다.
// 거창한 계획을 세운 전, 현, 승 세 사람은 서로 머리를 맞대고 고민하다가, 스트레스를 받아 연구를 집어치고 맥주를 마시러 떠나버렸습니다.
// 이를 본 여러분은 세 사람을 대신해 조건을 만족하는 간 레벨의 최솟값을 출력하는 프로그램을 만들어 주려고 합니다. 세 사람을 도와주세요!

// 입력
// 첫 번째 줄에 축제가 열리는 기간 N (1 ≤ N ≤ 200,000) 과, 채워야 하는 선호도의 합 M (1 ≤ M < 231) 과,
// 마실 수 있는 맥주 종류의 수 K (N ≤ K ≤ 200,000) 가 주어집니다.
// 다음 K개의 줄에는 1번부터 K번 맥주의 선호도 vi (0 ≤ vi ≤ 10,000) 와 도수 레벨 ci (1 ≤ ci < 231) (vi, ci는 정수) 이 공백을 사이에 두고 주어집니다.
// 1번부터 K번 맥주의 종류는 모두 다릅니다.

// 출력
// 첫 번째 줄에 주어진 선호도의 합 M을 채우면서 N개의 맥주를 모두 마실 수 있는 간 레벨의 최솟값을 출력합니다.
// 만약 아무리 레벨을 올려도 조건을 만족시킬 수 없으면 첫 번째 줄에 "-1" 하나만 출력하고 더 이상 아무것도 출력하지 않아야 합니다.

// 예제 입력 1 
// 3 9 5
// 2 5
// 4 6
// 3 3
// 4 3
// 1 4
// 예제 출력 1 
// 5

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

bool compare(pair<unsigned int, int>& a, pair<unsigned int, int>& b) {
    if (a.first == b. first) return a.second > b.second;
    return a.first < b.first;
}

int main() {
////////////////////
ios_base :: sync_with_stdio(false); 
cin.tie(NULL); 
cout.tie(NULL);

unsigned int n_of_days, m_of_satis, kind_of_beer;
cin >> n_of_days >> m_of_satis >> kind_of_beer;
vector<pair<unsigned int, int>> beer(kind_of_beer);
for (int k = 0; k < kind_of_beer; k++) {
    cin >> beer[k].second >> beer[k].first;
}
sort(beer.begin(), beer.end(), compare);

unsigned int satisfaction = 0;
priority_queue<int> choice;
for (int n = 0; n < n_of_days; n++) {
    choice.push(-beer[n].second);
    satisfaction += beer[n].second;
}
if (satisfaction >= m_of_satis) {
    cout << beer[n_of_days - 1].first;
    return 0;
}

for (int k = n_of_days; k < kind_of_beer; k++) {
    satisfaction += choice.top() + beer[k].second;
    choice.pop();
    choice.push(-beer[k].second);
    if (satisfaction >= m_of_satis) {
        cout << beer[k].first;
        return 0;
    }
}

cout << -1;
return 0;
////////////////////
}