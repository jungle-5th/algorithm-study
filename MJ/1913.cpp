// https://www.acmicpc.net/problem/1913
// 달팽이

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main() {

// arr[k][k] 배열 초기화
int k;
cin >> k;
int** arr = (int**) malloc(k * sizeof(int*));
for (int i = 0; i < k; i++) arr[i] = (int*) calloc(k, sizeof(int));
int mid = k/2;
arr[mid][mid] = 1;
// n_th_shell (n= 0 ~ ...) start from arr[mid-n][mid-n] num is (2n+1)^2
for (int n = 1; n <= mid; n++) {
    int o = mid-n;
    int top_num = (2*n + 1) * (2*n + 1);
    int bot_num = (2*n - 1) * (2*n - 1) + 1;
    int m1_num = bot_num + 2*n;
    int m2_num = top_num - 2*n;
    // 
    for (int i = 0; i < 2*n; i++) {
        arr[o+i][o] = top_num - i;
        arr[o][o+1+i] = bot_num + i; 
        arr[o+1+i][o+2*n] = m1_num + i;
        arr[o+2*n][o+i] = m2_num - i;
    }
}

int find;
cin >> find;
int x, y;
for (int i = 0; i < k; i++) {
    for (int j = 0; j < k; j++) {
        cout << arr[i][j] << " ";
        if (arr[i][j] == find) {
            x = i + 1;
            y = j + 1;
        }
    }
    cout << endl;
}
cout << x << ' ' << y;
for (int f = 0; f < k; f++) free(arr[f]);
free(arr);
arr = NULL;
}