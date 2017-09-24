#include <iostream>
#include <string>
#include <vector>

using namespace std;

int totalRuns(vector<int> bsl, vector<int> ps){
  int count = 0;
  int player = 0;
  for(int i=0; i<ps.size(); ++i){
    for(int j=0; j<3; ++j){
      if(bsl[player] >= ps[i]){
        cout << i << endl;
        ++count;
        break;
      }
      ++i;
    }
    ++player;
    if(player >= bsl.size()){
      break;
    }
  }
  // return count;
  if(count>=4){
    return count-3;
  }
  return 0;
}

int main(){
  vector<int> bsl {5,6,7,8,9};
  vector<int> ps {
    {10,10,5,10,5,7,8,9,10,10,10,10,10}
  };
  cout << totalRuns(bsl, ps) << endl;
  return 0;
}
