// https://www.acmicpc.net/problem/29791
// 에르다 노바와 오리진 스킬

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main () {
ios_base :: sync_with_stdio(false); 
cin.tie(NULL); 
cout.tie(NULL);
////////////////////////////////////
int nofnova, moforigin;
cin >> nofnova >> moforigin;
vector<int> nova(nofnova);
vector<int> origin(moforigin);
for (int n = 0; n < nofnova; n++) cin >> nova[n];
sort(nova.begin(), nova.end());
for (int m = 0; m < moforigin; m++) cin >> origin[m];
sort(origin.begin(), origin.end());

int novacool = 0, hold = 0, holdcount = 0;
for (int n = 0; n < nofnova; n++) {
    if (nova[n] >= novacool) {
        holdcount++;
        novacool = nova[n] + 100;
    }
}

int origincool = 0, stun = 0, stuncount = 0;
for (int m = 0; m < moforigin; m++) {
    if (origin[m] >= origincool) {
        stuncount++;
        origincool = origin[m] + 360;
    }
}

cout << holdcount << " " << stuncount;
////////////////////////////////////
return 0;}