#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

float getDistance(vector<int> a, vector<int> b){
  return sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2));
}

float maxXP(vector<vector<int>> grid, vector<int> pos, int num){
  priority_queue<float> pq;
  for(int i=0; i<grid.size(); ++i){
    for(int j=0; j<grid[0].size(); ++j){
      if(grid[i][j] > 0){
        float cost = getDistance({i,j}, pos);// + log10(grid[i][j]*1.0);
        float cp = grid[i][j]*1.0/cost;
        pq.push(cp);
      }
    }
  }

  float result = 0;
  for(int i = 0; i < num; ++i){
    result += pq.top(); pq.pop();
  }
  return result;
}

int main(){
  vector<vector<int>> g = {{0,1,10},{4,0,0},{0,0,0}};
  vector<int> p = {0,0};
  int n = 1;
  cout << maxXP(g,p,n) << endl;
  return 0;
}
