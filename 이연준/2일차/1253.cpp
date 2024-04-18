//// BOJ 1253 좋다

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, good = 0;
vector<long long> A;

int main() {
    cin >> N;
    A.resize(N);
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());

    for(int i = 0; i < N; i++) {
        int min = 0, max = N - 1;
        int target = A[i];
        while(min < max) {
            if(target < A[min] + A[max]) {
                max--;
            }
            else if(target > A[min] + A[max]) {
                min++;
            }
            else {
                if(min != i && max != i) {
                    good++;
                    break;
                }
                else if(min == i)   min++;
                else if(max == i)   max--;
            }
        }
    }

    cout << good;

    return 0;
}