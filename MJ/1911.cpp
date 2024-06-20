// https://www.acmicpc.net/problem/1911
// 흙길 보수하기

// 문제
// 어젯밤 겨울 캠프 장소에서 월드 본원까지 이어지는, 흙으로 된 비밀길 위에 폭우가 내려서 N(1 ≤ N ≤ 10,000)개의 물웅덩이가 생겼다.
// 월드학원은 물웅덩이를 덮을 수 있는 길이가 L(1 ≤ L ≤ 1,000,000)인 널빤지들을 충분히 가지고 있어서, 이들로 다리를 만들어 물웅덩이들을 모두 덮으려고 한다.
// 물웅덩이들의 위치와 크기에 대한 정보가 주어질 때, 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 구하여라.

// 입력
// 첫째 줄에 두 정수 N과 L이 들어온다.
// 둘째 줄부터 N+1번째 줄까지 총 N개의 줄에 각각의 웅덩이들의 정보가 주어진다. 웅덩이의 정보는 웅덩이의 시작 위치와 끝 위치로 이루어진다.
// 각 위치는 0 이상 1,000,000,000 이하의 정수이다. 입력으로 주어지는 웅덩이는 겹치지 않는다.

// 출력
// 첫째 줄에 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 출력한다.

// 예제 입력 1 
// 3 3
// 1 6
// 13 17
// 8 12
// 예제 출력 1 
// 5

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int>b) {
    return a.second > b.second;
}

int main() {
ios_base :: sync_with_stdio(false);
cin.tie(NULL); 
cout.tie(NULL);
///////////////////////////////////////////////
int n_of_puddle, l_of_panel;
cin >> n_of_puddle >> l_of_panel;
vector<pair<int, int>> puddles(n_of_puddle);
pair<int, int> puddle = {0,0};

for (int n = 0; n < n_of_puddle; n++) {
    cin >> puddle.first >> puddle.second;
    puddles[n] = puddle;
}

sort(puddles.begin(), puddles.end(), compare);
int panelpoint = 2000000000;
int result = 0;
for (int n = 0; n < n_of_puddle; n++) {
    pair<int, int> puddle = puddles[n];
    if (panelpoint > puddle.second) panelpoint = puddle.second;
    while (puddle.first < panelpoint) {
        panelpoint -= l_of_panel;
        result++;
    }
}
cout << result;
///////////////////////////////////////////////
return 0;}