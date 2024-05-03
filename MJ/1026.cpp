#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {


int n;
cin >> n;
vector<int> first_line(n);
for (int i = 0; i < n; i++) cin >> first_line[i];
vector<int> second_line(n);
for (int i = 0; i < n; i++) cin >> second_line[i];
sort(first_line.begin(), first_line.end());
sort(second_line.begin(), second_line.end(), greater<int>());
int res = 0;
for (int i = 0; i < n; i++) res += first_line[i]*second_line[i];
cout << res;


return 0;}