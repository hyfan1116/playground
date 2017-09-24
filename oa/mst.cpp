#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

struct edge{
  string a;
  string b;
  int weight;
  edge(string _a, string _b, int _weight){
    a = _a;
    b = _b;
    weight = _weight;
  }
};

struct _cmp{
  bool operator() (edge* lhs, edge* rhs){
    return lhs->weight < rhs->weight;
  }
} cmp;

int mst(vector<edge*> edges){
  int result = 0;
  unordered_set<string> spanned;
  sort(edges.begin(), edges.end(), cmp);
  for(int i=0; i<edges.size(); ++i){
    if(spanned.find(edges[i]->a) != spanned.end() &&
       spanned.find(edges[i]->b) != spanned.end() ){
      continue;
    }
    else{
      result += edges[i]->weight;
      spanned.insert(edges[i]->a);
      spanned.insert(edges[i]->b);
    }
  }
  return result;
}

int main(){

  vector<edge*> edges;
  edges.push_back(new edge("a", "b", 1));
  edges.push_back(new edge("a", "c", 1));
  //edges.push_back(new edge("a", "d", 1));
  edges.push_back(new edge("b", "c", 5));
  edges.push_back(new edge("b", "d", 5));
  edges.push_back(new edge("c", "d", 5));

  cout << mst(edges) << endl;

  return 0;
}
