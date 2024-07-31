// https://www.acmicpc.net/problem/20117
// 호반우 상인의 이상한 품질 계산법

// 문제
// 경북대 특산품 호반우는 품질에 따라 등급이 숫자로 매겨진다. 호반우 상인들은 N개의 호반우를 파려고 한다. 호반우는 개별적으로 팔 수도 있지만 묶음으로 팔 수도 있다.
// 이 때 묶음이라 함은 호반우들의 어떤 부분집합을 말한다. 하나의 호반우를 팔 때 기존의 계산법으로는 품질만큼의 가격으로 팔리게 된다.
// 따라서 묶어파나 개별적으로 파나 상인이 벌 수 있는 총 금액은 차이가 없었다. 하지만 호반우 상인들은 욕심쟁이여서 돈을 더 많이 받을 방법을 놓고 회의를 열게 된다.
// 그러던 와중 호반우 상인들은 새로운 품질 계산법을 개발해냈다! 호반우를 묶음으로 팔 때는 모든 호반우의 품질을 묶음의 '중앙값'으로 결정하게 된다.
// 이 때 묶음이 짝수인 경우 묶음 안에 있는 호반우를 품질을 기준으로 정렬했을 때 (묶음 개수/2+1)번째 호반우를 중앙값으로 정의하고 홀수인 경우 ((묶음 개수+1)/2)번째 호반우를 중간값으로 정의한다.
// 계산법을 새로 만드는 데는 성공했지만 호반우가 너무 많아 어떻게 묶어야 할 지 혼란이 오기 시작한 호반우 상인들은 장사에서 최대의 이익을 얻지 못 하고 있었다.
// 호반우 상인들을 위해 호반우들을 팔아서 얻을 수 있는 최대 이익을 계산하는 프로그램을 만들어주자!

// 입력
// 첫 번째 줄에 호반우의 개수 N (1 ≤ N ≤ 100,000)이 주어집니다.
// 두 번째 줄에 공백으로 구분된 N개의 정수 a1, a2, ..., an (1 ≤ ai ≤ 1,000)가 주어지는데 이 숫자는 각 호반우의 품질을 나타냅니다.

// 출력
// 모든 호반우를 팔았을 때 얻을 수 있는 최대 이익을 출력합니다.

// 예제 입력 1 
// 4
// 4 2 8 9
// 예제 출력 1 
// 34

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
///////////////////////////////////////////    
int n_of_cows; cin >> n_of_cows;
vector<int> cows(n_of_cows);
for (int n = 0; n < n_of_cows; n++) cin >> cows[n];
sort(cows.begin(), cows.end(), greater<>());
int cost = 0;
for (int m = 0; m < n_of_cows/2; m++) cost+=2*cows[m];
if (n_of_cows%2) cost+=cows[n_of_cows/2];
cout << cost;
///////////////////////////////////////////    
return 0;}