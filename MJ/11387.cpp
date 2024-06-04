// https://www.acmicpc.net/problem/11387
// 님 무기가 좀 나쁘시네여

#include <iostream>
using namespace std;

double min(double a, double b) {
    if (a < b) return a;
    else return b;
}

int main() {
double cri_first, pabu_first, cri_second, pabu_second;
double cri[5];
for (int i = 0; i < 5; i++) cin >> cri[i];
double pabu[5];
for (int i = 0; i < 5; i++) cin >> pabu[i];
double weapon1[5];
for (int i = 0; i < 5; i++) cin >> weapon1[i];
double weapon2[5];
for (int i = 0; i < 5; i++) cin >> weapon2[i];

cri_first = cri[0] * (1 + cri[1]/100) * ((1-min(cri[2]*0.01, 1)) + min(cri[2]*0.01, 1)*cri[3]*0.01)*(1+cri[4]*0.01);
pabu_first = pabu[0] * (1 + pabu[1]/100) * ((1-min(pabu[2]*0.01, 1)) + min(pabu[2]*0.01, 1)*pabu[3]*0.01)*(1+pabu[4]*0.01);
for (int i = 0; i < 5; i++) {
    cri[i] = cri[i]-weapon1[i]+weapon2[i];
    pabu[i] = pabu[i]-weapon2[i]+weapon1[i];
}

cri_second = cri[0] * (1 + cri[1]*0.01) * ((1-min(cri[2]*0.01, 1)) + min(cri[2]*0.01, 1)*cri[3]*0.01)*(1+cri[4]*0.01);
pabu_second = pabu[0] * (1 + pabu[1]*0.01) * ((1-min(pabu[2]*0.01, 1)) + min(pabu[2]*0.01, 1)*pabu[3]*0.01)*(1+pabu[4]*0.01);

if (cri_first > cri_second) cout << '-';
else if (cri_first < cri_second) cout << '+';
else cout << 0;

cout << endl;

if (pabu_first > pabu_second) cout << '-';
else if (pabu_first < pabu_second) cout << '+';
else cout << 0;

return 0;}