#include <iostream>
#include <vector>

using namespace std;

int main(){

int n_of_boxes;
int k_of_rules;
int d_of_dotori;
cin >> n_of_boxes >> k_of_rules >> d_of_dotori;
vector<vector<int>> rules(k_of_rules,vector<int>(3));
for (int i = 0; i < k_of_rules; i++) cin >> rules[i][0] >> rules[i][1] >> rules[i][2];

vector<int> boxes(n_of_boxes+1, 0);

for (int rule = 0; rule < k_of_rules; rule++) {
    int start = rules[rule][0];
    int end = rules[rule][1];
    int interval = rules[rule][2];
    for (int j = 0; j < ((end-start)/interval + 1); j++) {
        boxes[start + j * interval] += 1;
    }
}

int boxnum = 1;
while(d_of_dotori > 0) {
    d_of_dotori -= boxes[boxnum];
    boxnum++;
}

cout << (boxnum-1);
}