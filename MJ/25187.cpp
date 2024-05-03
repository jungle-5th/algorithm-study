// https://www.acmicpc.net/problem/25187
// 고인물이 싫어요

// 문제
// 재형이는 청정수를 좋아하고 고인물을 싫어한다. 오늘도 청정수를 구하기 위해 물탱크들이 있는 마을에 방문한다.
// 마을에는 N개의 물탱크가 존재하고, 각 물탱크는 청정수 또는 고인물을 저장하고 있다. 그리고 물탱크는 공급의 편의를 위해 M개의 파이프로 서로 연결되어 있다.
// 청정수를 얻기 위해 K번 물탱크에 방문했을 때, K번 물탱크와 K번 물탱크에서 0개 이상의 파이프를 거쳐 이동 가능한 물탱크 중,
// 청정수가 담긴 물탱크의 수가 고인물이 담긴 물탱크의 수보다 더 많은 경우 청정수를 얻을 수 있다.
// 방문할 예정인 물탱크에 대한 정보가 주어질 때마다, 청정수를 얻을 수 있는지 구해보자. 

// 입력
// 첫째 줄에 물탱크의 수 N(1 <= N <= 100000)과 파이프의 수 M(0 <= M <= 200000), 그리고 물탱크에 방문할 횟수 Q(1 <= Q <= 100000)가 주어진다. 
// 둘째 줄에 1번부터 N번 물탱크까지 순서대로 들어있는 물의 종류가 주어진다. 청정수는 1, 고인물은 0으로 주어진다. 
// 다음 3번째부터 M+2번째 줄까지 파이프가 연결하는 두 물탱크의 번호 u, v(1 <= u, v <= N, u <= v)가 주어진다.
// 같은 두 물탱크를 연결하는 파이프가 여러 개 존재할 수 있다. M+3번째부터 M+Q+2번째 줄까지 방문할 물탱크의 번호 K(1 <= K <= N)가 주어진다.  

// 출력
// Q개의 줄에 각 물탱크에 방문했을 때 청정수를 얻을 수 있다면 1을, 아니면 0을 주어진 정보 순서대로 출력한다. 

// 예제 입력 1 
// 5 3 3
// 1 0 1 1 0
// 1 2
// 3 4
// 4 5
// 1
// 5
// 4
// 예제 출력 1 
// 0
// 1
// 1

#include <iostream>
using namespace std;

static int *flag;
static int find_union(int tank);

int main() {

int n_of_tanks;
int m_of_pipes;
int q_of_visits;

cin >> n_of_tanks >> m_of_pipes >> q_of_visits;

int *water_quality = (int *) calloc((n_of_tanks+1), sizeof(int));
for (int i = 1; i <= n_of_tanks; i++) {
    int input_q;
    cin >> input_q;
    water_quality[i] = (input_q==1 ? 1 : -1);
}

int *sumres = (int*) calloc((n_of_tanks+1), sizeof(int));

flag = (int *) malloc((n_of_tanks+1) * sizeof(int));
for (int i = 0; i <= n_of_tanks; i++) {
    flag[i] = i;
}

for (int i = 0; i < m_of_pipes; i++) {
    int p1, p2;
    cin >> p1 >> p2;
    if (find_union(p1) != find_union(p2)) {
        flag[find_union(p2)] = flag[p1];
    }
}

for (int i = 1; i <= n_of_tanks; i++) {
    sumres[find_union(i)] += water_quality[i];
}

for (int q = 0; q < q_of_visits; q++) {
    int tank;
    cin >> tank;
    if (sumres[find_union(tank)] > 0) cout << 1 << "\n";
    else cout << 0 << "\n";

}

free(water_quality);
free(flag);
free(sumres);

return 0;
}


static int find_union(int tank) {
    if (flag[tank] == tank) return tank;
    else {
        flag[tank] = find_union(flag[tank]);
        return flag[tank];
    }
}


// vector<vector<bool>> adj_matrix((n_of_tanks+1), vector<bool>((n_of_tanks+1),0));

// bool **adj_matrix = (bool **) malloc((n_of_tanks+1)*sizeof(bool *));
// for (int row = 0; row <= n_of_tanks; row++) {
//     adj_matrix[row] = (bool*) calloc(n_of_tanks+1, sizeof(bool));
// }


// for (int i = 0; i < m_of_pipes; i++) {
//     int p1, p2;
//     cin >> p1 >> p2;
//     adj_matrix[p1][p2] = 1;
//     adj_matrix[p2][p1] = 1;
// }


// for (int via = 1; via <= n_of_tanks; via++){
//     for (int from = 1; from <= n_of_tanks; from++) {
//         for (int to = 1; to <= n_of_tanks; to++) {
//             adj_matrix[from][to] = adj_matrix[from][to] | (adj_matrix[from][via] & adj_matrix[via][to]);
//         }
//     }
// }

// for (int i = 0; i < q_of_visits; i++) {
//     int tank;
//     cin >> tank;
//     int sum = 0;
//     for (int j = 1; j <= n_of_tanks; j++) {
//         sum += adj_matrix[tank][j]*water_quality[j];
//     }
//     cout << (sum > 0);
// }

// for (int i = 0; i <= n_of_tanks+1; i++) {
//     free(adj_matrix[i]);
// }

// free(adj_matrix);