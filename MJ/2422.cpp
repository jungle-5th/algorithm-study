// https://www.acmicpc.net/problem/2422
// 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

// 문제
// 한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다. 아이스크림 가게에는 N종류의 아이스크림이 있다.
// 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다.
// 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때, 선택하는 방법이 몇 가지인지 구하려고 한다.

// 입력
// 첫째 줄에 정수 N과 M이 주어진다. N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수이다.
// 아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다. 같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

// 출력
// 첫째 줄에, 가능한 방법이 총 몇 개 있는지 출력한다.

// 예제 입력 1 
// 5 3
// 1 2
// 3 4
// 1 3
// 예제 출력 1 
// 3

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
//////////////////////////////////////
int n_of_icecream, m_of_bans;
cin >> n_of_icecream >> m_of_bans;

vector<vector<int>> bans(n_of_icecream+1);
for (int m = 0; m < m_of_bans; m++) {
    int a, b;
    cin >> a >> b;
    if (a>b) bans[b].push_back(a);
    else bans[a].push_back(b);
}

int count = 0;
for (int i = 1; i < n_of_icecream-1; i++) {
    for (int j = i+1; j < n_of_icecream; j++) {
        if (find(bans[i].begin(), bans[i].end(), j) != bans[i].end()) continue;
        for (int k = j + 1; k <= n_of_icecream; k++) {
            if (find(bans[j].begin(), bans[j].end(), k) != bans[j].end()) continue;
            if (find(bans[i].begin(), bans[i].end(), k) != bans[i].end()) continue;
            count++;
        }
    }
}
cout << count;
//////////////////////////////////////
return 0;}