#include <iostream>
#include <algorithm>
#include <exception>
#include <string>
#include <regex>

using namespace std;

vector<int> logParse(string s){
  vector<int> lp;
  regex rgx("(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2})Z");
  smatch m;
  if(regex_search(s, m, rgx)){
    for(size_t i=1; i<m.size(); ++i){
      lp.push_back(stoi(m[i].str()));
    }
  }
  else{
    throw invalid_argument("invalid date time");
  }
  return lp;
}

int logCompare(string lhs, string rhs){
  try{
    vector<int> l = logParse(lhs);
    vector<int> r = logParse(rhs);
    for(int i=0; i<6; ++i){
      if(l[i] != r[i]){
        return l[i] - r[i];
      }
    }
  }
  catch(exception& e){
    cout << e.what() << endl;
  }
  return 0;
}

vector<string> logSearch(vector<string> logs, string ts0, string ts1){
  vector<string> res;
  for(auto s : logs){
    if(logCompare(ts0, s) <= 0 && logCompare(s,ts1) <= 0){
      res.push_back(s);
    }
  }
  return res;
}

int main(){
  /*
  string ts0, ts1;
  cout << "input timestamps" << endl;
  cin >> ts0 >> ts1;
  cout << "input log size" << endl;
  int size;
  cin >> size;

  cout << "input " << size << " entries" << endl;
  vector<string> logs;
  string tmp;
  for(int i=0; i<size; ++i){
    cin >> tmp;
    logs.push_back(tmp);
  }
  */

  string ts0 = "2016-02-12T03:21:55Z hello";
  string ts1 = "2016-02-12T03:22:00Z bye";
  vector<string> logs {
    "2016-02-12T03:21:56Z abcd",
    "2016-02-12T03:21:59Z efgh",
    "2016-02-12T03:22:02Z ijkl",
    "2016-02-12T03:23:51Z mnop",
  };

  vector<string> res;
  res = logSearch(logs, ts0, ts1);

  cout << "results: " << endl;
  for(auto s : res){
    cout << s << endl;
  }

  return 0;
}
