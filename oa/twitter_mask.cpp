#include <iostream>
#include <algorithm>
#include <string>
#include <regex>

using namespace std;

string mask(string input){
  string output;

  regex r1("(\\w+)@\\w+.com");
  smatch m1;
  if(regex_search(input, m1, r1)){
    string user(m1.length(1), '*');
    user[0] = input[0];
    user[m1.position(1)+m1.length(1)-1] =
      input[m1.position(1)+m1.length(1)-1];
    output = user + input.substr(m1.position(1) + m1.length(1));
    return output;
  }

  regex r2("^(\\(\\d{3}\\)\\d{3})-\\d{4}$");
  smatch m2;
  if(regex_search(input, m2, r2)){
    output = "(***)***"+input.substr(m2.position(1) + m2.length(1));
    return output;
  }

  regex r3("^(\\+1\\(\\d{3}\\)\\d{3})-\\d{4}$");
  smatch m3;
  if(regex_search(input, m3, r3)){
    output = "+*(***)***"+input.substr(m3.position(1) + m3.length(1));
    return output;
  }

  return output;
}

int main(){
  string s1 = "hyfan@gmail.com";
  string s2 = "(314)562-0048";
  string s3 = "+1(314)562-0048";

  cout << mask(s1) << endl;
  cout << mask(s2) << endl;
  cout << mask(s3) << endl;
  return 0;
}
