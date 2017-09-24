#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <priority_queue>

using namespace std;

struct cmp{
  bool operator()(vector<int> lhs, vector<int> rhs){
    return lhs[2] < rhs[2];
  }
};

vector<int> mx = {1,-1,0,0};
vector<int> my = {0,0,1,-1};

int calcDark(vector<vector<int>> inks, vector<vector<int>>& pool){
  //queue<pair<int,int>> q;
  priority_queue<vector<int>, vector<vector<int>>, cmp> pq;
  for(auto ink : inks){
    pq.push(ink);
  }

  while(!pq.empty()){
      vector<int> cur = pq.top(); pq.pop();
      if(pool[get<0>(cur)][get<1>(cur)] < get<2>(cur)){

      }
  }

  int sum = 0;
  for(int i=0; i<pool.size();++i){
    for(int j=0; j<pool[0].size(); ++j){
      sum += pool[i][j];
      cout << pool[i][j] << ' ';
    }
    cout << endl;
  }

  return sum;
}

int main(){
  /*
  int m,n;
  cin >> m >> n;
  vector<vector<int>> pool (m, vector<int>(n,0));
  */
  vector<vector<int>> pool (5, vector<int>(6,0));
  /*
  int size_ink;
  cin >> size_ink;
  vector<tuple<int, int, int>> inks;
  for(int i=0; i<size_ink; ++i){
    int row, col, darkness;
    cin >> row >> col >> darkness;
    inks.push_back(make_tuple(row, col, darkness));
  }
  */
  vector<vector<int>> inks {
    {1,0,10},
    {2,2,9},
    {2,3,5},
    {4,2,9}
  };

  int res = calcDark(inks, pool);
  cout << res << endl;
  return 0;
}
