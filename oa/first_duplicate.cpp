#include <iostream>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <utility>

using namespace std;

string first_duplicate(string s){
  unordered_set<string> hash;
  istringstream iss(s);
  string tmp;
  while(iss >> tmp){
    //cout << tmp << endl;
    if(hash.find(tmp) != hash.end()){
      return tmp;
    }
    hash.insert(tmp);
  }
  return "";
}

string earliest_duplicate(string s){
  unordered_map<string,int> hash;
  istringstream iss(s);
  int i = 0;
  string tmp;
  int index = s.size();
  string result = "";
  while(iss >> tmp){
    //cout << tmp << endl;
    if(hash.find(tmp) == hash.end()){
      hash[tmp] = i;
    }
    else{
      if(index > hash[tmp]){
        index = hash[tmp];
        result = tmp;
      }
    }
    ++i;
  }

  return result;
}

int main(){
  string s = "dog cat fish cat dog";
  cout << first_duplicate(s) << endl;
  return 0;
}
