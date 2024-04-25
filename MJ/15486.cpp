// sort로 인한 시간초과 이후 자건풀이법 이용

#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {

int n_of_days;
cin >> n_of_days;
// jobs = {job0, job1 .... job(n-1)}
// job = {endday, startday, pay}
vector<vector<int>> jobs(n_of_days+1,vector<int>(3, 0));
for (int i = 1; i <= n_of_days; i++) {
    int man_day;
    int pay;
    cin >> man_day >> pay;
    int end_day = i + man_day - 1;
    jobs[i] = {end_day, pay};
}
// sort(jobs.begin(), jobs.end());

vector<int> p(n_of_days+2, 0);

for (int j = n_of_days; j > 0; j--) {
    if (jobs[j][0] > n_of_days) {
        p[j] = p[j+1];
        continue;
    }
    if (p[j+1] < (p[jobs[j][0]+1] + jobs[j][1])) p[j] = (p[jobs[j][0]+1] + jobs[j][1]);
    else p[j] = p[j+1];
    // cout << p[j] << endl;
}

cout << p[1];

}
