//encoding:utf-8
//#include <iostream> //c++
//#include<stack> //スタックに関して　最新のデータから捨てる
//#include<queue> //キューに関して　最古のデータから捨てる
//#include<math.h>
//#include<vector>
//#include<algorithm> //sort とかにいる
#include<bits/stdc++.h>//vector,algorithm,que
#include<time.h> //時間にかんして

#define ll long long
#define MOD 1000000007
using namespace std;
int main(){
  int N,K;
  cin>>N>>K;
  ll number = 1;
  for(int i=0;i<N;i++){
    if(number>K){
      number += K;
    }
    else{
      number = number*2;
    }
  }
  cout<<number<<endl;

  return 0;
}
