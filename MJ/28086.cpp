// https://www.acmicpc.net/problem/28086
// 미소녀 컴퓨터 파루빗토 쨩.

// 문제
// 미소녀 컴퓨터 파루빗토 쨩은 SCSC에서 만든 8비트 컴퓨터의 이름(일 수도 있었던 무언가)이다.
// 파루빗토 쨩은 파루빗토로 작동하며 파루빗토 덧셈, 파루빗토 뺄셈, 파루빗토 곱셈, 파루빗토 나눗셈을 할 수 있다.
// 그런데 파루빗토 컴퓨터를 만든 SCSC 동아리원들은 수많은 전선을 연결하다 눈이 침침해진 나머지 잘못 연결한 전선이 있을까 걱정되기 시작했다!
// 파루빗토 쨩이 잘 작동하는지 검증하기 위한 코드를 작성해보자!

// 입력
// 첫째 줄에 A+B, A-B, A*B, A/B 중 하나의 형태의 수식이 주어진다. 입력에 공백이 포함되지 않으며, +-나 --의 형태의 연산자는 주어지지 않고, 
// A와 B는 모두 8진수 정수이다. (-o1000000000 <= A,B <= o1000000000) 제한 범위는 8진수 기준이다. 즉, 10진수 기준으로는 -8^9 <= A,B <= 8^9 이다.

// 출력
// 주어진 수식의 계산 결과를 8진수 정수로 출력한다. 이때 나눗셈은 floor A/B로 계산한다. 수식을 계산할 수 없는 경우 invalid를 출력한다.

// 예제 입력 1 
// 14+16
// 예제 출력 1 
// 32
// 예제 입력 2 
// 4*4
// 예제 출력 2 
// 20
// 예제 입력 3 
// 63/-2
// 예제 출력 3 
// -32
// 예제 입력 4 
// 4022/0
// 예제 출력 4 
// invalid
// 예제 입력 5 
// 777777777-1000000000
// 예제 출력 5 
// -1

#include <stdio.h>

long octal(long dec) {
    long oct = 0;
    long digit = 1;
    while(dec) {
        oct += (dec%10)*digit;
        dec = dec/10;
        digit = digit*8;
    }
    return oct;
}
long deciaml(long oct) {
    long dec = 0;
    long digit = 1;
    while (oct) {
        dec += (oct%8)*digit;
        oct = oct/8;
        digit = digit*10;
    }
    return dec;
}

int main() {
//////////////////////////////

long a, b;
char oper;

char inputstr[100];
fgets(inputstr, 100, stdin);
sscanf(inputstr, "%ld%c%ld", &a,&oper,&b);
a = octal(a);
b = octal(b);
long c;

if (oper == '+') c = a + b;
else if (oper == '-') c = a - b;
else if (oper == '*') c = a * b;
else {
    if (b == 0) {
        printf("invalid");
        return 0;
    }
    else if ((a*b) < 0) {
        if ((a%b) == 0) c = a/b;
        else c = a/b-1;
    }
    else c = a/b;
}

if (c < 0) {
    c = -c;
    long res = deciaml(c);
    printf("-%ld",res);
}
else {
    long res = deciaml(c);
    printf("%ld",res);
}
//////////////////////////////
return 0;}