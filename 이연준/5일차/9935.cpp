/// BOJ 9935 문자열 폭발

#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

string input, bomb;

int main() {
    cin >> input;
    cin >> bomb;
    int N = input.length();
    int bombsz = bomb.length();
    stack<pair<char, int>> str;

    for(int i = 0; i < N; i++) {
        if(!str.empty() && str.top().second == bombsz) {
            int cnt = bombsz;
            while(cnt--) {
                str.pop();
            }
        }
        if(!str.empty() && str.top().second != 0) {
            if(input[i] == bomb[str.top().second]) {
                str.push({input[i], str.top().second + 1});
            }
            else if(input[i] == bomb[0]) {
                str.push({input[i], 1});
            }
            else{
                str.push({input[i], 0});
            }
        }
        else if(input[i] == bomb[0]) {
            str.push({input[i], 1});
        }
        else {
            str.push({input[i], 0});
        }
    }
    if(str.top().second == bombsz) {
        int cnt = bombsz;
        while(cnt--) {
            str.pop();
        }
    }
    stack<char> result;
    while(!str.empty()) {
        char ch = str.top().first;
        str.pop();
        result.push(ch);
    }
    if(result.empty()) {
        cout << "FRULA";
    }
    else {
        while(!result.empty()) {
            cout << result.top();
            result.pop();
        }
    }

    return 0;
}