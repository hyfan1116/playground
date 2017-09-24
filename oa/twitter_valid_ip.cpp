#include <iostream>
#include <exception>
#include <string>
#include <regex>

using namespace std;

bool isIPv4(string s){
  regex r("^(\\d{1,3}\\.){3}\\d{1,3}$");
  smatch m;
  return regex_search(s, m, r);
}

bool isIPv6(string s){
  regex r("^(\\w{1,4}\\:){7}\\w{1,4}$");
  smatch m;
  return regex_search(s, m, r);
}

string validate(string s){
  if(isIPv4(s)){
    return "IPv4";
  }
  else if(isIPv6(s)){
    return "IPv6";
  }
  else{
    return "Neither";
  }
}

int main(){
  string ip1 = "121.18.19.20";
  string ip2 = "2001:0db8:0000:0000:0000:ff00:0042:8329";
  string ip3 = "3:0db8:0:00:000:ff0:0042:8329";
  string ip4 = "3:0db8:0:00:000:ff0";
  string ip5 = "127.1.1";

  cout << validate(ip1) << endl;
  cout << validate(ip2) << endl;
  cout << validate(ip3) << endl;
  cout << validate(ip4) << endl;
  cout << validate(ip5) << endl;

  return 0;
}
