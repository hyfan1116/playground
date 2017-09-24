#include <iostream>

using namespace std;

void reverseString(string& s, int l, int r) {
    //int l = 0;
    //int r = s.size() - 1;
    if(r - l < 1){
        return;
    }

    while(l < r){
        char tmp = s[l];
        s[l] = s[r];
        s[r] = tmp;
        ++l;
        --r;
    }
    return;
}

void reverseHTML(string& s){
  int start = -1;
  int end = -1;
  for(int i=0; i<s.size(); ++i){
    if(s[i] == '&'){
      start = i;
    }
    else if(s[i] == ';' && start != -1){
      reverseString(s, start, i);
      start = -1;
    }
  }

  reverseString(s, 0, s.size() - 1);
}

int main(){
  string s = "hello world &aa&hyf;;;an";
  reverseHTML(s);
  cout << s << endl;
  return 0;
}
