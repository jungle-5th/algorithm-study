// https://www.acmicpc.net/problem/5073
// 삼각형과 세 변

// 문제
// 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
// Equilateral :  세 변의 길이가 모두 같은 경우
// Isosceles : 두 변의 길이만 같은 경우
// Scalene : 세 변의 길이가 모두 다른 경우
// 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
// 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
// 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

// 입력
// 각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

// 출력
// 각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

// 예제 입력 1 
// 7 7 7
// 6 5 4
// 3 2 5
// 6 2 6
// 0 0 0
// 예제 출력 1 
// Equilateral
// Scalene
// Invalid
// Isosceles

#include <stdio.h>
int main() {
    int a,b,c;
    while (1){
        scanf("%d %d %d", &a,&b,&c);
        if (a==0 && b==0 && c==0) return 0;
        if (a>=(b+c) || b>=(c+a) || c>=(a+b)) printf("Invalid\n");
        else if (a==b && b==c) printf("Equilateral\n");
        else if (a!=b && b!=c && c!=a) printf("Scalene\n");
        else printf("Isosceles\n");
    }
return 0;}