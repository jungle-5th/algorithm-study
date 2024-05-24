/// BOJ 28086  미소녀 컴퓨터 파루빗토 쨩

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string input;

int OtoI(string str) {
    long long num = stoi(str);
    int p = 0;
    int ret = 0;
    while(num != 0) {
        if(num % 10 >= 8) {
            return 2147483647;
        }
        ret += (num % 10) * pow(8, p);
        num /= 10;
        p++;
    }
    return ret;
}

string ItoO(long long num) {
    string ret = "";
    while(num != 0) {
        ret = to_string(num % 8) + ret;
        num /= 8;
    }
    return ret;
}

int main() {
    cin >> input;
    if(input.find('+') != string::npos) {
        int idx = input.find('+');
        long long a = OtoI(input.substr(0, idx));
        long long b = OtoI(input.substr(idx + 1));
        if(a == 2147483647 || b == 2147483647) {
            cout << "invalid";
            return 0;
        }
        long long res = a + b;
        if(res < 0) {
            cout << "-" + ItoO(-res);
        }
        else if(res > 0){
            cout << ItoO(res);
        }
        else {
            cout << 0;
        }
    }
    else if(input.find('*') != string::npos) {
        int idx = input.find('*');
        long long a = OtoI(input.substr(0, idx));
        long long b = OtoI(input.substr(idx + 1));
        if(a == 2147483647 || b == 2147483647) {
            cout << "invalid";
            return 0;
        }
        
        long long res = a * b;
        if(res < 0) {
            cout << "-" + ItoO(-res);
        }
        else if(res > 0){
            cout << ItoO(res);
        }
        else {
            cout << 0;
        }
    }
    else if(input.find('/') != string::npos) {
        int idx = input.find('/');
        long long a = OtoI(input.substr(0, idx));
        long long b = OtoI(input.substr(idx + 1));
        if(a == 2147483647 || b == 2147483647) {
            cout << "invalid";
            return 0;
        }
    
        if(b == 0) {
            cout << "invalid";
        }
        else {
            long long res = floor((float)a / (float)b);
            if(res < 0) {
            cout << "-" + ItoO(-res);
            }
            else if(res > 0){
                cout << ItoO(res);
            }
            else {
                cout << 0;
            }
        }
    }
    else if(input.find('-') != string::npos) {
        int idx = input.find('-');        
        if(input.find('-') == 0) {
            idx = input.find('-', 1);
        }
        long long a = OtoI(input.substr(0, idx));
        long long b = OtoI(input.substr(idx + 1));
        if(a == 2147483647 || b == 2147483647) {
            cout << "invalid";
            return 0;
        }
        
        long long res = a - b;
        if(res < 0) {
            cout << "-" + ItoO(-res);
        }
        else if(res > 0){
            cout << ItoO(res);
        }
        else {
            cout << 0;
        }
    }
    else {
        cout << "invalid";
    }

    return 0;
}