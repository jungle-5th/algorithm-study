#include <iostream>
using namespace std;

int main() {
ios_base :: sync_with_stdio(false); 
cin.tie(NULL); 
cout.tie(NULL);
//////////////////////////////////////////////////
int n; cin >> n;
long long countZero = 0, countOne = 0, countOther = 0;
for (int i=0;i<n;i++){
    int num; cin >> num;
    if (num==0) countZero++;
    else if (num==1) countOne++;
    else countOther++;        
}
long long ans =countOne*countZero*2 + countOther*countZero + (countZero*(countZero-1))/2;
cout << ans;
//////////////////////////////////////////////////
return 0;}