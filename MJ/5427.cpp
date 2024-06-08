// https://www.acmicpc.net/problem/5427
// 불

// 문제
// 상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.
// 매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다.
// 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.
// 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

// 입력
// 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개이다.
// 각 테스트 케이스의 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)
// 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.

// '.': 빈 공간
// '#': 벽
// '@': 상근이의 시작 위치
// '*': 불
// 각 지도에 @의 개수는 하나이다.

// 출력
// 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다. 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

#include <vector>
#include <iostream>
#include <queue>
#include <array>
using namespace std;

int main() {
///////////////////////////////////////////
int testcase;
cin >> testcase;
for (int t = 0; t < testcase; t++){
    int width, height;
    cin >> width >> height;
    vector<vector<char>> map(height, vector<char>(width));
    queue<array<int,3>> fire;
    queue<array<int,3>> man;
    for (int h = 0; h < height; h++) {
        for (int w = 0; w < width; w++) {
            cin >> map[h][w];
            if (map[h][w] == '*') fire.push({h,w,0});
            else if (map[h][w] == '@') {
                man.push({h,w,0});
                map[h][w] = '#';
            }
        }
    }

    vector<pair<int,int>> direction = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    // int turn = 0;
    bool escape = false;
    while (!escape && !man.empty()) {
        int fq = fire.size();
        int mq = man.size();
        for (int fi = 0; fi < fq; fi++) {
            array<int,3> f = fire.front(); fire.pop();
            for (int d = 0; d < 4; d++) {
                int y = f[0] + direction[d].first;
                int x = f[1] + direction[d].second;
                if (y >= 0 && y < height && x >= 0 && x < width && map[y][x] == '.') {
                    map[y][x] = '*';
                    fire.push({y,x,f[2]+1});
                }
            }
        }
        for (int mi = 0; mi < mq; mi++) {
            array<int,3> m = man.front(); man.pop();
            for (int d = 0; d < 4; d++) {
                int y = m[0] + direction[d].first;
                int x = m[1] + direction[d].second;
                if (y < 0 || y >= height || x < 0 || x >= width) {
                    cout << m[2] + 1 << endl;
                    escape = true;
                    break;
                }
                else if (map[y][x] == '.') {
                    map[y][x] = '#';
                    man.push({y,x,m[2]+1});
                }
            }
            if (escape) break;
        }
    }
    if (!escape) cout << "IMPOSSIBLE" << endl;
}
///////////////////////////////////////////
return 0;}