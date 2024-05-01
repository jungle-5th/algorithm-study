// https://www.acmicpc.net/problem/26085
// 효구와 호규 (Easy)

// 문제
// 효구는 N개의 행과 M개의 열로 이루어진 N X M 크기의 격자판을 갖고 있다. 각 칸에는 하나의 카드가 놓여 있으며, 카드에는 0 또는 1의 숫자가 적혀 있다.
// 깔끔한 걸 좋아하는 형 호규는 격자판의 모든 카드를 없애려고 한다. 단, 호규는 아래의 두 가지 행동만을 원하는 만큼 수행할 수 있다.
// 동일한 숫자를 가진 두 카드가 인접해 있으면 두 카드를 없앤다.
// 카드 하나를 골라 카드가 없는 인접한 칸으로 옮긴다.
// 여기서 인접해 있다는 것은 상하좌우 네 방향 중 한 방향으로 인접해 있음을 의미한다.
// 호규가 모든 카드를 없앨 수 있는지 알아보자.

// 입력
// 첫 번째 줄에는 격자판의 크기를 나타내는 두 정수 N과 M이 주어진다. (3 <= N, M <= 1000)

// 두 번째 줄부터 
// N+1 번째 줄까지는 격자판의 정보가 주어진다. 각 줄에는 M개의 숫자가 공백으로 구분되어 주어지며, i+1번째 줄의 j번째 숫자는 i행 j열에 놓인 카드의 숫자를 의미한다.
// 단, 각 숫자는 0 또는 1이다.

// 출력
// 모든 카드를 없앨 수 있으면 1을 출력하고, 그렇지 않으면 -1을 출력한다.

// 예제 입력 1 
// 3 4
// 0 1 0 1
// 1 1 0 0
// 1 0 1 0
// 예제 출력 1 
// 1

#include <iostream>
using namespace std;

int main(){

int n, m;
cin >> n >> m;
if ((n*m)%2) {cout <<-1; return 0;}

bool even = 1;
bool last;
bool now;
bool pre_row;
bool adj = 0;

// first row
cin >> pre_row;
last = pre_row;
if (last) even = !even;
for (int j = 1; j < m; j++) {
    cin >> now;
    if (now) even = !even;
    if (last == now) adj = 1;
    last = now;
}


// second row~
for (int i = 1; i < n; i++) {
    cin >> last;
    if (last) even = !even;
    if (pre_row == last) adj = 1;
    pre_row = last;

    for (int j = 1; j < m; j++) {
        cin >> now;
        if (now) even = !even;
        if (last == now) adj = 1;
        last = now;
    }
}

if (adj & even) cout << 1;
else cout << -1;

return 0;
}