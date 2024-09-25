// https://www.acmicpc.net/problem/20310
// 타노스

#include <iostream>
#include <deque>
using namespace std;

int main() {
////////////////////////////////////////////
string str; cin >> str;
deque<int> zeroq;
deque<int> oneq;
for (int i = 0; i < str.size(); i++) {
    if (str[i] == '0') zeroq.push_back(i);
    else oneq.push_back(i);
}
int zs = zeroq.size(), os = oneq.size();
for (int i = 0; i < zs/2; i++) zeroq.pop_back();
for (int i = 0; i < os/2; i++) oneq.pop_front();

deque<char> res;
while (!zeroq.empty() && !oneq.empty()) {
    if (zeroq.front() < oneq.front()) {res.push_back('0');zeroq.pop_front();}
    else {res.push_back('1');oneq.pop_front();}
}
while (!zeroq.empty()) {res.push_back('0');zeroq.pop_front();}
while (!oneq.empty()) {res.push_back('1');oneq.pop_front();}

while (!res.empty()) {cout<<res.front();res.pop_front();}
////////////////////////////////////////////
return 0;}