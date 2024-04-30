// https://www.acmicpc.net/problem/24460
// 특별상이라도 받고 싶어

// 문제
// HCPC 2021에 참석한 N x N명의 사람들이 의자가 정사각형 형태로 배치된 대회장에서 대회를 한다.
// 모든 의자에는 서로 다른 추첨번호가 적혀있으며 HCPC 2021의 마지막에는 아래에 설명된 규칙에 따라 특별상을 받을 사람 한 명을 정한다.
// 특별상을 받을 수 있는 사람이 한 명이라면, 그 사람이 뽑힌다.
// 그렇지 않은 경우, 대회장을 같은 크기의 정사각형 네 개로 나누어 각 구역에서 이 규칙을 재귀적으로 적용해서 구역마다 한 명씩 총 네 명을 뽑는다.
// 뽑힌 네 명 중 의자에 적힌 추첨번호가 두 번째로 작은 사람이 뽑힌다.
// HCPC 2021에 참가한 지원이는 자신의 실력이 부족해서 수상권이 아니라고 생각하였고, 실력과 무관하게 받을 수 있는 특별상을 노리고 있다.
// 의자 각각에 적혀 있는 추첨번호가 주어질 때, 지원이가 HCPC 2021에서 경품을 받을 수 있으려면 어떤 의자에 앉아야 하는지 계산하는 프로그램을 작성하시오.

// 입력
// 첫 번째 줄에는 정수 N이 주어진다. (단,N = 2^m, 0 <= m <= 10, m은 정수)
// 두 번째 줄부터 N개 줄의 i번째 줄에는 i번째 줄에 있는 의자에 적힌 추첨번호가 주어진다. 각 줄에는 N개의 추첨번호가 공백으로 구분되어 주어진다.
// 추첨번호는 2^31 보다 작은 음이 아닌 정수이고, 모든 추첨번호는 서로 다름이 보장된다.

// 출력
// 지원이가 HCPC 2021에서 경품을 받기 위해 앉아야 하는 의자에 적힌 추첨번호를 출력한다.

// 예제 입력 1 
// 2
// 2 0
// 3 1
// 예제 출력 1 
// 1

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

int pick_second(int a, int b, int c, int d) {
    int arr[4] = {a,b,c,d};
    sort(arr, end(arr));
    return arr[1];
}

int contest(int y, int x, int n ,int **map) {
    if (n == 2) return pick_second(map[y][x], map[y+1][x], map[y][x+1], map[y+1][x+1]);
    return pick_second(contest(y,x,n/2,map), contest(y+n/2,x,n/2,map), contest(y,x+n/2,n/2,map), contest(y+n/2,x+n/2,n/2,map));
}

int main() {
int n_of_square;
cin >> n_of_square;

if (n_of_square == 1) {
    int res;
    cin >> res;
    cout << res;
    return 0;
}

int** map = (int**) malloc(n_of_square * sizeof(int*));
for (int i = 0; i < n_of_square; i++) map[i] = (int*) calloc(n_of_square, sizeof(int));
// vector<vector<int>> map (n_of_square, vector<int>(n_of_square, 0));
for (int i = 0; i < n_of_square; i++) {
    for (int j = 0; j < n_of_square; j++) cin >> map[i][j];
}

cout << contest(0,0,n_of_square,map); 

for (int i = 0; i < n_of_square; i++) free(map[i]);
free(map);
return 0;
}