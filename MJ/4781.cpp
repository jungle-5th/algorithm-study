// https://www.acmicpc.net/problem/4781
// 사탕 가게

// 문제
// 상근이는 선영이와 걸어가다가 사탕 가게를 지나가게 되었다. 갑자기 상근이는 선영이에게 사탕이 얼마나 건강에 안 좋은지 설명하기 시작했다.
// 선영이는 매우 짜증이 났고, 상근이에게 누가 더 건강이 안 좋아질 수 있는지 내기를 하자고 했다. 상근이는 내기를 그 즉시 받아들였다.
// 두 사람은 같은 돈을 가지고 가게에 들어가서 사탕을 산다. 이때, 구매한 사탕의 칼로리가 더 큰 사람이 내기에서 이기게 된다.
// 상근이는 잠시 화장실에 갔다온다고 핑계를 댄 뒤에, 노트북을 열고 사탕 가게의 시스템을 해킹하기 시작했다.
// 이 시스템에는 현재 사탕 가게에 있는 사탕의 가격과 칼로리가 모두 등재되어 있다. 각 사탕의 개수는 매우 많기 때문에, 원하는 만큼 사탕을 구매할 수 있다.
// 또, 사탕은 쪼갤 수 없기 때문에, 일부만 구매할 수 없다.
// 사탕 가게에 있는 모든 사탕의 가격과 칼로리가 주어졌을 때, 어떻게 하면 칼로리의 합이 가장 크게 되는지를 구하는 프로그램을 작성하시오.

// 입력
// 각 테스트 케이스의 첫째 줄에는 가게에 있는 사탕 종류의 수 n과 상근이가 가지고 있는 돈의 양 m이 주어진다.
// (1 ≤ n ≤ 5,000, 0.01 ≤ m ≤ 100.00) m은 항상 소수점 둘째자리까지 주어진다.
// 다음 n개 줄에는 각 사탕의 칼로리 c와 가격 p가 주어진다. (1 ≤ c ≤ 5,000, 0.01 ≤ p ≤ 100.00) c는 항상 정수, p는 항상 소수점 둘째자리이다.
// 입력의 마지막 줄에는 '0 0.00'이 주어진다.

// 출력
// 각 테스트 케이스에 대해서, 상근이가 돈 m을 가지고 구매할 수 있는 가장 높은 칼로리를 출력한다.

// 예제 입력 1 
// 2 8.00
// 700 7.00
// 199 2.00
// 3 8.00
// 700 7.00
// 299 3.00
// 499 5.00
// 0 0.00

// 예제 출력 1 
// 796
// 798

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main() {

while (true) {
    int n_of_candies;
    double money_double;
    // n_of_candies와 money_double 입력 받기
    cin >> n_of_candies >> money_double;

    // 0 0.00이면 탈출
    if (n_of_candies == 0 && money_double == 0.00) break;

    // 가진돈 x.yz에서 xyz원으로 변환
    money_double = 100 * money_double;
    int money_int = static_cast<int>(round(money_double));
    
    // cout << money_int;

    // 가게 사탕 정보 받기
    vector<vector<int>> candies(n_of_candies,vector<int>(2));
    for (int i = 0; i < n_of_candies; i++) {
        int cal;
        double cost_double;
        int cost_int;
        cin >> cal >> cost_double;
        cost_double = 100 * cost_double;
        cost_int = static_cast<int>(round(cost_double));
        candies[i] = {cal, cost_int};
    }

    // DP테이블 만들기 n_of_candies + 1개 행, money_int + 1개 열.
    int ** dptable = (int**) calloc(n_of_candies+1, sizeof(int*));
    for (int i = 0; i <= n_of_candies; i++) dptable[i] = (int*) calloc(money_int+1, sizeof(int));


    // DP테이블 채우기
    for (int row = 1; row <= n_of_candies; row++) {
        int cal_of_this = candies[row-1][0];
        int cost_of_this = candies[row-1][1];
        for (int column = 1; column <= money_int; column++) {
            if (column >= cost_of_this) {
                dptable[row][column] = max(dptable[row-1][column], cal_of_this + dptable[row][column - cost_of_this]);
            }
            else dptable[row][column] = dptable[row-1][column];
        }
    }

    // dptable[n_of_candies][money_int] 값 출력
    cout << dptable[n_of_candies][money_int] << endl;

    // 메모리 관리
    for (int i = 0; i <= n_of_candies; i++) free(dptable[i]);
    free(dptable);
}

}
