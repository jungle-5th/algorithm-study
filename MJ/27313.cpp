// https://www.acmicpc.net/problem/27313
// 효율적인 애니메이션 감상

// 문제
// 애니메이션 애호가이면서도 PS 애호가인 한별이는, 어느 날 PS를 하느라 보지 못한 애니메이션이 N개나 된다는 것을 깨달았다!
// 그러나, PS를 너무 오랫동안 하지 않으면 solved.ac 스트릭이 깨지는 불상사를 당하기 때문에 한별이는 애니메이션을 최대 M시간 동안만 보기로 했다.
// 이에 한별이는 애니메이션을 동시에 최대 K개씩 묶어서 보기로 했는데, 한별이가 동시에 애니메이션을 보는 방법은 다음과 같다.
// 애니메이션을 보고 있지 않은 상태에서, 한별이는 아직 보지 않은 애니메이션 중 K개 이하의 애니메이션을 동시에 보기 시작한다.
// 애니메이션을 보고 있는 도중에는 새로운 애니메이션을 보기 시작할 수 없다.
// 이로 인해, 한별이는 보기 시작한 애니메이션 중에서 가장 긴 애니메이션이 끝날 때까지 다른 애니메이션을 보기 시작할 수 없다.
// 한별이는 애니메이션 시청의 달인이기 때문에 애니메이션이 끝남과 동시에 새로운 애니메이션을 보기 시작할 수 있다.
// N개의 애니메이션 각각을 보는 데에 걸리는 시간이 주어질 때, M시간 동안 볼 수 있는 애니메이션의 최대 개수를 구하시오.

// 입력
// 첫 번째 줄에 한별이가 봐야 하는 애니메이션의 개수 N, 한별이가 애니메이션을 보는 데에 사용할 수 있는 시간을 나타내는 정수 M,
// 한별이가 동시에 볼 수 있는 애니메이션의 개수 K가 공백으로 구분되어 주어진다. (1 <= N <= 100000, 0 <= M <= 10^9, 1 <= K <= 100000)
// 두 번째 줄에 N개의 애니메이션 각각을 보는 데에 걸리는 시간을 나타내는 정수 l_i가 공백으로 구분되어 주어진다. (1 <= l_i <= 10^9)

// 출력
// 한별이가 볼 수 있는 애니메이션의 최대 개수를 출력한다.

// 예제 입력 1 
// 2 3 4
// 3 4
// 예제 출력 1 
// 1
// 예제 입력 2 
// 3 15 2
// 10 5 10
// 예제 출력 2 
// 3

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
///////////////////////////////////////////
int allani, time, bracket_size;
cin >> allani >> time >> bracket_size;
if (allani < bracket_size) bracket_size = allani; // exception when bracket size is bigger
int mox = allani / bracket_size;
int remainder = allani % bracket_size;
vector<int> ani(allani);
vector<int> bracket(bracket_size);
for (int a = 0; a < allani; a++) cin >> ani[a];

sort(ani.begin(), ani.end());

// memoization for 1 cycle
for (int i = 0; i < bracket_size; i++) {
    bracket[i] = ani[i];
    if (ani[i] > time) {
        cout << i;
        return 0;
    }
}

// find end bracket
int end_bracket = 1;
int result = ani[bracket_size-1];
for (int i = 2; i <= mox; i++) {
    result += ani[bracket_size*i-1];
    if (result > time) break;
    end_bracket = i;
}

if (end_bracket < mox) remainder = bracket_size; 

for (int i = remainder-1; i >=0; i--) {
    result = 0;
    for (int j = 0; j <= end_bracket; j++) {
        result += ani[bracket_size*j+i];
    }
    if (result <= time) {
        cout << (end_bracket*bracket_size+i+1);
        return 0;
    }
}

cout << end_bracket*bracket_size;
///////////////////////////////////////////
return 0;}