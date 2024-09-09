// https://www.acmicpc.net/problem/1244
// 스위치 켜고 끄기


#include <iostream>
#include <vector>
using namespace std;

int main() {
/////////////////////////////////////
int nOfSwitches; cin >> nOfSwitches;
vector<int> onOff (nOfSwitches+1);
for (int n = 1; n <= nOfSwitches; n++) cin >> onOff[n];
int students; cin >> students;
for (int s = 0; s < students; s++) {
    int sex, num; cin >> sex >> num;
    if (sex == 1) {
        for (int i = 1; i <= nOfSwitches / num; i++) {
            if (i*num <= nOfSwitches) onOff[i*num] = 1-onOff[i*num];
        }
    }
    else if (sex == 2) {
        int range = 0;
        while (true) {
            if (num+range > nOfSwitches || num-range < 1) break;
            if (onOff[num-range] == onOff[num+range]) {
                onOff[num-range] = 1-onOff[num-range];
                onOff[num+range] = onOff[num-range];
                range++;
            }
            else break;
        }
    }
}

int count = 1;
for (int i = 1; i <= nOfSwitches; i++) {
    cout << onOff[i] << " ";
    if (count%20 == 0) cout << "\n";
    count ++;
}
/////////////////////////////////////
}