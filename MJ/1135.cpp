// https://www.acmicpc.net/problem/1135
// 뉴스 전하기

// 문제
// 민식이는 회사의 매니저이다. 그리고, 민식이는 회사의 중요한 뉴스를 모든 직원에게 빠르게 전달하려고 한다. 민식이의 회사는 트리 구조이다.
// 모든 직원은 정확하게 한 명의 직속 상사가 있다. 자기자신은 그들 자기 자신의 직접 또는 간접 상사가 아니고, 모든 직원은 민식이의 직접 또는 간접적인 부하이다.
// 민식이는 일단 자기 자신의 직속 부하에게 한 번에 한 사람씩 전화를 한다. 뉴스를 들은 후에, 각 부하는 그의 직속 부하에게 한 번에 한 사람씩 전화를 한다.
// 이 것은 모든 직원이 뉴스를 들을 때 까지 계속된다. 모든 사람은 자신의 직속 부하에게만 전화를 걸 수 있고, 전화는 정확하게 1분 걸린다.
// 이때 모든 직원이 소식을 듣는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
// 오민식의 사원 번호는 0이고, 다른 사원의 번호는 1부터 시작한다.

// 입력
// 첫째 줄에 직원의 수 N이 주어진다. 둘째 줄에는 0번 직원부터 그들의 상사의 번호가 주어진다.
// 0번 직원 (오민식)은 상사가 없기 때문에 -1이고, 나머지 직원 i의 상사 번호는 i보다 작거나 같은 음이 아닌 정수이다. N은 50보다 작거나 같은 자연수이다.

// 출력
// 첫째 줄에 모든 소식을 전하는데 걸리는 시간의 최솟값을 출력한다.

// 예제 입력 1 
// 3
// -1 0 0
// 예제 출력 1 
// 2

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <vector<int>> boss (50);

int mintime(vector<int> bos) {
    if (bos.size() == 0) return 0;

    // 각 서브트리 연락망의 최소 전파시간을 수집
    vector<int> results;
    for (int i = 0; i < bos.size(); i++) {
        results.push_back(mintime(boss[bos[i]]));
    }

    // 서브트리중 가장 오래걸리는 연락망부터 전화를 돌린다.
    sort(results.begin(), results.end(), greater<int>());
    for (int i = 0; i < bos.size(); i++) {
        results[i] += (1+i);
    }

    // 그렇게 해서 나온 결과 중 가장 마지막까지 전파되는 시간이 내 연락망의 최소 전파시간
    sort(results.begin(), results.end(), greater<int>());
    return results[0];
}


int main() {
// ios_base :: sync_with_stdio(false); 
// cin.tie(NULL); 
// cout.tie(NULL);
/////////////////////////////////////////////

int workers;
int nothing;
cin >> workers >> nothing;

// make tree
for (int w = 1; w < workers; w++) {
    int b;
    cin >> b;
    boss[b].push_back(w);
}

cout << mintime(boss[0]);


/////////////////////////////////////////////
return 0;}


