#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {

int n_of_days;
cin >> n_of_days;
vector<vector<int>> jobs(n_of_days,vector<int>(3));
for (int i = 0; i < n_of_days; i++) {
    int man_day;
    int pay; 
    cin >> man_day >> pay;
    int end_day = i + man_day;
    jobs[i] = {end_day, i + 1, pay};
}

sort(jobs.begin(), jobs.end());

// for (int i = 0; i < n_of_days; i++) {
//     cout << jobs[i][0] << " " << jobs[i][1] << " " << jobs[i][2] << endl;
// }

vector<int> p(n_of_days+1, 0);

for (int i = 1; i <= n_of_days; i++) {
    p[i] = p[i-1];
    while (jobs[0][0] == i) {
        p[i] = max(p[i], p[jobs[0][1]-1] + jobs[0][2]);
        // cout << jobs[0][0] << jobs[0][1] << jobs[0][2] << endl;
        if (jobs.size() == 1) break;
        jobs.erase(jobs.begin());
    }
}

// for (int j = 0; j <= n_of_days; j++) p[j];

cout << p[n_of_days];
}
