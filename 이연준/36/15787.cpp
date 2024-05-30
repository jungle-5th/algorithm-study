/// BOJ 15787 기차가 어둠을 헤치고 은하수를

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int N, M;
vector<string> order;

int main() {
    cin >> N >> M;
    vector<int> train(N + 1, 0);
    for(int i = 0; i < M; i++) {
        // cout << "기차의 현재 상태 \n";
        // for(int j = 1; j <= N; j++) {
        //     cout << j << "번 열차 : " << train[j] << endl;
        // }
        int order_num;
        cin >> order_num;
        int train_num;
        int seat_num;
        if(order_num == 1) {
            cin >> train_num >> seat_num;
            // cout << train_num << "번 열차의 " << seat_num << "번 좌석에 사람을 태웁니다\n";
            // cout << "이전 현황 : " << train[train_num] << endl;
            train[train_num] = train[train_num] | (1 << seat_num);
            // cout << "이후 현황 : " << train[train_num] << endl;
        }
        else if(order_num == 2) {
            cin >> train_num >> seat_num;
            // cout << train_num << "번 열차의 " << seat_num << "번 좌석을 하차시킵니다\n";
            // cout << "이전 현황 : " << train[train_num] << endl;
            train[train_num] = train[train_num] & ~(1 << seat_num);
            // cout << "이후 현황 : " << train[train_num] << endl;
            
        }
        else if(order_num == 3) {
            cin >> train_num;
            // cout << train_num << "번 열차의 " << "사람들을 한칸씩 뒤로 미룹니다다\n";
            // cout << "이전 현황 : " << train[train_num] << endl;
            train[train_num] = (train[train_num] << 1) & ~(1 << 21);
            // cout << "이후 현황 : " << train[train_num] << endl;
        }
        else {
            cin >> train_num;
            // cout << train_num << "번 열차의 " << "사람들을 한칸씩 앞으로로로 미룹니다다\n";
            // cout << "이전 현황 : " << train[train_num] << endl; 
            train[train_num] = (train[train_num] >> 1) & ~1;
            // cout << "이후 현황 : " << train[train_num] << endl;
        }
    }
    set<int> galaxy;
    for(int i = 1; i <= N; i++) {
        galaxy.insert(train[i]);
    }
    // for(auto iter = galaxy.begin(); iter != galaxy.end(); iter++) {
    //     cout << *iter << endl;
    // }
    cout << galaxy.size();

    return 0;
}