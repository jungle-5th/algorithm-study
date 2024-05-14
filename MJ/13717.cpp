// https://www.acmicpc.net/problem/13717
// 포켓몬 GO

// 모바일 게임을 즐겨 하는 지우는 Jetpack Joyride 에 금새 질렸고 포켓몬 GO를 시작했다! 이 게임의 재미있는 점은 포켓몬을 진화시킬 수 있다는 것이다.
// 지우가 Pi 라는 포켓몬을 진화시키기 위해서는 해당 포켓몬의 Ki 개의 사탕이 필요하다. 진화가 된 후에는 2개의 사탕을 돌려받는다.
// 각 포켓몬은 그들 종의 사탕으로만 진화할 수 있다.
// 지우는 N종의 포켓몬이 있고 Pi 라는 포켓몬의 사탕은 Mi 개를 가지고 있으며 지우는 진화시킬 수 있는 포켓몬의 총 마리수를 궁금해한다.
// 또한, 지우는 가장 많이 진화시킬 수 있는 포켓몬이 무엇인지 알고 싶어한다. 만약 그런 포켓몬들이 여러 종이 있다면 도감번호가 가장 작은 포켓몬을 출력한다.
// 즉, 입력 데이터에서 더 먼저 나타나는 포켓몬을 출력하면 된다. 

// 입력
// 첫 번째 줄에는 포켓몬의 종류 수를 나타내는 N (1 ≤ N ≤ 70)이 주어진다.
// 그 다음 2N 줄에는 N개의 데이터 세트가 입력되는데 2i 번째 줄에는 i번째 포켓몬의 이름을 나타내는 최대길이 20의 Pi 문자열이 주어진다.
// 2i + 1 번째 줄에는 Ki  (12 ≤ Ki ≤ 400) , Mi (1 ≤ Mi ≤ 104) 가 주어지는데
// 각각 i 번째 포켓몬이 진화에 필요한 사탕의 수와 지우가 가지고 있는 i 번째 포켓몬의 총 사탕의 수이다.

// 출력
// 첫 번째 줄엔 진화시킬 수 있는 포켓몬의 총 마리수를 출력한다.
// 두 번째 줄엔 가장 많이 진화시킬 수 있는 포켓몬의 이름을 출력한다.

// 예제 입력 1 
// 4
// Caterpie
// 12 33
// Weedle
// 12 42
// Pidgey
// 12 47
// Rattata
// 25 71
// 예제 출력 1 
// 14
// Weedle

#include <iostream>
#include <string>
using namespace std;

int main() {
 
int pokemons;
cin >> pokemons;
int maxevo=0;
int evo=0;
string most_evo;
for (int i = 0; i < pokemons; i++) {
    string poke;
    int need, have;
    int evocount = 0;
    int ee;
    cin >> poke >> need >>have;
    while((ee = (have / need)) > 0){
          evocount += ee;
          have += 2*ee - ee*need;          
    }
    evo += evocount;
    if(evocount > maxevo) {
        maxevo = evocount;
        most_evo = poke;
    }
}
    cout << evo << endl << most_evo;
return 0;}