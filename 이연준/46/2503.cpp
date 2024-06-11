/// BOJ 2503 숫자 야구

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int N;

int main() {
    cin >> N;
    vector<pair<string, pair<int, int>>> bb(N);
    for(int i = 0; i < N; i++) {
        string str;
        int strk, ball;
        cin >> str >> strk >> ball;
        bb[i] = {str, {strk, ball}};
    }
    int answer = 0;
    for(int i = 1; i <= 9; i++) {
        for(int j = 1; j <= 9; j++) {
            if(j == i)  continue;
            for(int k = 1; k <= 9; k++) {
                if(k == j || k == i)    continue;
                bool flag = true;
                for(auto turn : bb) {
                    string str = turn.first;
                    int strk = turn.second.first;
                    int ball = turn.second.second;
                    int s = 0;
                    int b = 0;
                    
                    if(str[0] - '0' == i) {
                        s++;
                    }
                    else if(str.find(to_string(i)) != string::npos) {
                        b++;
                    }
                    if(str[1] - '0' == j) {
                        s++;
                    }
                    else if(str.find(to_string(j)) != string::npos) {
                        b++;
                    }
                    if(str[2] - '0' == k) {
                        s++;
                    }
                    else if(str.find(to_string(k)) != string::npos) {
                        b++;
                    }
                    if(strk != s || ball != b) {
                        flag = false;
                        break;
                    }
                }
                if(flag) {
                    answer++;
                }
            }
        }
    }
    cout << answer;

    return 0;
}