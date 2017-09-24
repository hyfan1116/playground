#include <iostream>
#include <algorithm>
#include <utility>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

const char nb[4] = {'A', 'C', 'T', 'G'};

int findMutationDistance(unordered_set<string>& bank_set,
  string start, string end){

  unordered_set<string> visited;
  visited.insert(start);
  queue<pair<string, int>> q;
  q.push(make_pair(start, 0));
  while(!q.empty()){
    pair<string, int> curp = q.front(); q.pop();

    string curr = curp.first;
    int count = curp.second;
    if(curr == end){
      return count;
    }

    cout << "curr: " << curr << endl;

    //string next = curr;
    for(int i=0; i<8; ++i){
      string next = curr;
      for(int j=0; j<4; ++j){
        next[i] = nb[j];
        if(bank_set.find(next) != bank_set.end()){
          if(visited.find(next) == visited.end()){
            visited.insert(next);
            q.push(make_pair(next, count+1));
          }
        }
      }
    }
  }
  return -1;
}

int main(){
  string start ="AAAAAAAA";
  string end = "AAAAAATT";
  vector<string> bank = {
    "AAAAAAAA",
    "AAAAAAAT",
    "AAAAAATT",
    "AAAAATTT",
    "GAAAAAAA"
  };

  unordered_set<string> bank_set (bank.begin(), bank.end());

  cout << findMutationDistance(bank_set, start ,end) << endl;
  return 0;
}
