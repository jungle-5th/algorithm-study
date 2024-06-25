// https://www.acmicpc.net/problem/11728
// 배열 합치기

// 문제
// 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
// 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

// 출력
// 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

// 예제 입력 1 
// 2 2
// 3 5
// 2 9
// 예제 출력 1 
// 2 3 5 9

// 예제 입력 2 
// 2 1
// 4 7
// 1
// 예제 출력 2 
// 1 4 7

// 예제 입력 3 
// 4 3
// 2 3 5 9
// 1 4 7
// 예제 출력 3 
// 1 2 3 4 5 7 9

const fs = require("fs")
const filePath = process.platform === "linux" ? '/dev/stdin' : "/input.txt";
let input = fs.readFileSync(__dirname+filePath).toString().trim().split("\n");

function main() {
    let arr1 = input[1].split(" ");
    let arr2 = input[2].split(" ");
    let union = arr1.concat(arr2);
    union = union.map(str => parseInt(str));
    union.sort((a,b) => a-b);
    let res = "";
    union.forEach((any) => res += (any) + " ");
    return res;
}
console.log(main());