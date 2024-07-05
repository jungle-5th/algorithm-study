// https://www.acmicpc.net/problem/11727
// 2xn 타일링 2

// 문제
// 2xn 직사각형을 1x2, 2x1과 2x2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

// 출력
// 첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

// 예제 입력 1 
// 2
// 예제 출력 1 
// 3

#include <stdio.h>
int main() {
int a, res = 1;
scanf("%d",&a);
for(int i = 0; i < a; i++) {
    if (i%2) res = res*2+1;
    else res = res*2-1;
    res = res%10007;
}
printf("%d",res);
return 0;}