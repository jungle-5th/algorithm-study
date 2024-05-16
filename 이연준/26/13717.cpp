/// BOJ 13717 포켓몬 GO

#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int N;
vector<string> num;
map<string, pair<int, int>> candy;
map<string, int> evolution;

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        string pokemon; cin >> pokemon;
        int K, M;   cin >> K >> M;
        candy[pokemon] = {K, M};
        evolution[pokemon] = 0;
        num.push_back(pokemon);
    }
    int answer = 0;
    for(auto iter = candy.begin(); iter != candy.end(); iter++) {
        string pokemon = iter->first;
        int need = (iter->second).first;
        int have = (iter->second).second;
        while(have / need != 0) {
            int can = have / need;
            evolution[pokemon] += can;
            answer += can;
            have -= can * need;
            have += 2 * can;
        }
    }
    string max_pok;
    int MAX_ev = 0;
    for(int i = 0; i < N; i++) {
        if(evolution[num[i]] > MAX_ev) {
            max_pok = num[i];
            MAX_ev = evolution[num[i]];
        }
    }
    cout << answer << "\n";
    cout << max_pok;

    return 0;
}