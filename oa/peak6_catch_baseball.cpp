#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> signX {1,1,-1,-1};
vector<int> signY {1,-1,1,-1};
bool canCatch(int ballX, int ballY,
              vector<vector<int>> players, vector<int> reaches){
  //unordered_set<vector<int>> positions;
  for(int i=0; i<players.size(); ++i){
    int px = players[i][0];
    int py = players[i][1];
    int reach = reaches[i];
    if(px*ballY == py*ballX){
      return true;
    }
    for(int j=0; j<=reach; ++j){
      for(int k=0; k<=reach-j; ++k){
        int cx, cy;
        for(int sign = 0; sign < 4; ++sign){
          cx = px + signX[sign]*k;
          cy = py + signY[sign]*j;
          cout << cx << ' ' << cy << endl;
          if(cx*ballY == cy*ballX){
            return true;
          }
        }
      }
    }
  }

  return false;
}

int main(){
  int bx = 3;
  int by = 4;
  vector<vector<int>> ps {{0,5}};
  vector<int> rs {5};
  cout << canCatch(bx,by,ps,rs) << endl;
  return 0;
}
