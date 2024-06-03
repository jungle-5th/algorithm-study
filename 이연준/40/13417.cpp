/// BOJ 13417 카드 문자열

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--) {
        int N;  cin >> N;
        vector<char> ch(N);
        for(int i = 0; i < N; i++) {
            cin >> ch[i];
        }
        string answer;
        answer = ch[0] + answer;
        for(int i = 1; i < N; i++) {
            if(answer[0] >= ch[i]) {
                answer = ch[i] + answer;
            }
            else {
                answer = answer + ch[i];
            }
        }
        cout << answer << "\n";
    }

    return 0;
}