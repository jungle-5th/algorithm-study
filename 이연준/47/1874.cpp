/// BOJ 스택 수열

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    int n;
    stack<int> st;
    vector<int> seq(n);
    for(int i = 0; i < n; i++) {
        cin >> seq[i];
    }
    int idx = 0;
    vector<char> ans;
    for(int i = 1; i <= n; i++) {
        st.push(i);
        ans.push_back('+');
        while(!st.empty() && st.top() == seq[idx]) {
            st.pop();
            ans.push_back('-');
            idx++;
        }
    }
    if(!st.empty()) {
        cout << -1;
    }
    else {
        for(int i = 0; i < ans.size(); i++) {
            cout << ans[i] << "\n";
        }
    }

    return 0;
}