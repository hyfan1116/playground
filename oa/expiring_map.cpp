#include <iostream>
#include <unordered_map>

using namespace std;

class ExpMap{
  int currentTime;
  unordered_map<int, string> key_val;
  unordered_map<int, long> key_dur;
  unordered_map<int, long> key_start;
public:
  ExpMap():
  currentTime(0)
  {}

  void put(int key, string value, long duration){
    if(key_val.find(key) == key_val.end()){
      key_val[key] = value;
      key_dur[key] = duration;
      //key_start[key] = start_time;
    }
    else{
      key_val[key] = value;
      key_dur[key] = duration;
      // update start_time
      // move to end of list
    }
  }

  string get(int key){
    // update the list
    if(key_val.find(key) == key_val.end()){
      return "";
    }
    else{
      return key_val[key];
    }
  }
};

int main(){
  ExpMap em;
  em.put(1, "hello", 100);
  string result = em.get(1);
  cout << result << endl;
  return 0;
}
