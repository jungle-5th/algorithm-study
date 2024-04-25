/// BOJ 21314 민겸 수

#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int main() {
    string input;   cin >> input;

    string MIN, MAX;
    stack<char> min;
    stack<char> max;

    for(int i = 0; i < input.length(); i++) {
        // 최대값 만들기
        if(max.empty()) {
            max.push(input[i]);
        }
        else if(max.top() == 'M') {                                 // max의 top이 M인 경우
            if(input[i] == 'M') max.push(input[i]);
            else {
                MAX += '5';
                while(!max.empty()) {
                    MAX += '0';
                    max.pop();
                }
            }
        }
        else {                                                      // max의 top이 K인 경우
            MAX += '5';
            max.pop();
            while(!max.empty()) {
                MAX += '0';
                max.pop();
            }
            max.push(input[i]);
        }
        // 최소값 만들기
        if(min.empty()) {
            min.push(input[i]);
        }
        else if(min.top() == 'M') {                                 // min의 top이 M인 경우
            if(input[i] == 'M') {
                min.push(input[i]);
            }
            else {
                MIN += '1';
                for(int j = 0; j < min.size() - 1; j++) MIN += '0';
                MIN += '5';
                while(!min.empty()) min.pop();
            }
        }
        else {                                                      // max의 top이 K인 경우
            MIN += '5';
            min.pop();
            min.push(input[i]);
        }
    }
    if(!max.empty()) {
        if(max.top() == 'K') {
            MAX += '5';
            max.pop();
            while(!max.empty()) {
                MAX += '0';
                max.pop();
            }
        }
        else {
            while(!max.empty()) {
                MAX += '1';
                max.pop();
            }
        }
    }
    if(!min.empty()) {
        if(min.top() == 'M') {
            MIN += '1';
            for(int j = 0; j < min.size() - 1; j++) MIN += '0';
        }
        else {
            MIN += '5';
            for(int j = 0; j < min.size() - 1; j++) MIN += '0';
        }
    }
    cout << MAX << endl;
    cout << MIN;
    return 0;
}