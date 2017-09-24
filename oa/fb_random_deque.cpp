#include <iostream>
#include <algorithm>

#include <vector>
#include <list>
#include <deque>

using namespace std;

class random_list{
  deque<int> dq;
public:
  random_list(vector<int> input){
    //sort(input.begin(), input.end());
    for(auto i : input){
      dq.push_back(i);
    }
  }

  int pop(){
    int tmp;
    if(rand()%2) {
      tmp = dq.back();
      dq.pop_back();
    }
    else {
      tmp = dq.front();
      dq.pop_front();
    }
    return tmp;
  }

  int peek(){
    if(rand()%2) return dq.back();
    else return dq.front();
  }

  bool isEmpty(){
    return dq.empty();
  }

  void printCurrent(){
    for(auto i : dq){
      cout << i << ' ';
    }
    cout << endl;
  }

};

vector<int> retrieve(random_list rl){
  vector<int> front;
  list<int> back;

  if(rl.isEmpty()) return vector<int>();

  int pk = rl.peek();
  int pp = rl.pop();
  int lpk,lpp;
  bool ud = false;

  if(pk > pp){
    front.push_back(pp);
  }
  else if(pk < pp){
    back.push_front(pp);
  }
  else{
    ud = true;
  }
  lpk = pk;
  lpp = pp;

  while(!rl.isEmpty()){
    pk = rl.peek();
    pp = rl.pop();
    if(ud){
      if(lpp < pp) front.push_back(lpp);
      else back.push_front(lpp);
      ud = false;
    }
    if(pk > pp){
      front.push_back(pp);
    }
    else if(pk < pp){
      back.push_front(pp);
    }
    else{
      ud = true;
    }
    lpk = pk;
    lpp = pp;
  }

  if(ud){
    front.push_back(lpp);
  }

  for(int i : back){
    front.push_back(i);
  }

  return front;
}

int main(){
  vector<int> input {1,2,3,4,5,6,7};
  random_list rl (input);

  /*
  while(!rl.isEmpty()){
    cout << rl.pop() << endl;
    rl.printCurrent();
  }
  */

  vector<int> output;
  output = retrieve(rl);

  for(auto i : output){
    cout << i << ' ';
  }
  cout << endl;

  return 0;
}
