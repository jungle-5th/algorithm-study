// https://www.acmicpc.net/problem/10974
// 모든 순열

// 문제
// N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

// 출력
// 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

// 예제 입력 1 
// 3
// 예제 출력 1 
// 1 2 3
// 1 3 2
// 2 1 3
// 2 3 1
// 3 1 2
// 3 2 1

const fs = require("fs");
const filePath = process.platform === "linux" ? '/dev/stdin' : "/input.txt";
let input = fs.readFileSync(__dirname + filePath).toString().trim().split("\n");

function permul(set, str) {
    if (set.length == 1) {
        let newstr = str + set[0]
        console.log(newstr)
        return
    }

    for (let i = 0; i < set.length; i++) {
        let num = set[i]
        let newstr = str + num + " "
        set.splice(i,1)
        permul(set, newstr)
        set.splice(i, 0, num)
    }
}

function main(n) {
    let set = []
    let str = ""
    for (let q = 1; q <= n; q++) {set.push(q)}
    permul(set, str)
}

main(parseInt(input[0]))