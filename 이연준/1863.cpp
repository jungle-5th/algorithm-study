/// BOJ 1863 스카이라인 쉬운거

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    int n;
    cin >> n;
    stack<int> sky;
    for(int i = 0; i < n; i++) {
        int a, h;   cin >> a >> h;
        if(sky.empty()) {
            sky.push(h);
        }
        else {
            if(sky.top() < h) {
                int prev;
                while(prev = sky.top() < h && !sky.empty()) {
                    
                }
            }
            else {

            }
        }
    }

    return 0;
}