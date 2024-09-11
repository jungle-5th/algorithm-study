// https://www.acmicpc.net/problem/17266
// 어두운 굴다리

#include <iostream>
using namespace std;

int main() {
ios_base::sync_with_stdio(false);
cin.tie(NULL);
//////////////////////////////////////////////////////////
int length, num; cin >> length >> num;
int h; cin >> h;
int location = h;
int idx = location + h;
for (int n = 1; n < num; n++) {
    cin >> location;
    if (location - h > idx) {
        h = (location-idx+h+1)/2;
    }
    idx = location + h;
}
if (idx < length) h = length - location;

cout << h;
//////////////////////////////////////////////////////////
return 0;}