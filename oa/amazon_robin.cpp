#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct process{
  int arr_time;
  int exe_time;
  process(int _arr_time, int _exe_time){
    arr_time = _arr_time;
    exe_time = _exe_time;
  }
};

double rount_robin(vector<int> arr, vector<int> exe, int a){
  int cur = 0;
  int wait = 0;
  int idx = 1;
  queue<process*> q;
  q.push(new process(arr[0], exe[0]));
  while(!q.empty()){
    process* tmp = q.front(); q.pop();
    wait += (cur - tmp->arr_time);
    cout << cur << ' ' << tmp->exe_time << endl;
    if(tmp->exe_time <= a){
      cur += tmp->exe_time;
    }
    else{
      cur += a;
    }

    while(arr[idx]<=cur && idx < arr.size()){
      q.push(new process(arr[idx],exe[idx]));
      ++idx;
    }

    if(tmp->exe_time > a){
      q.push(new process(cur, tmp->exe_time - a));
    }
  }

  return wait*1.0/(arr.size());

}

int main(){
  vector<int> arr = {0,1,3,9};
  vector<int> exe = {2,1,7,5};
  cout << rount_robin(arr,exe,2) << endl;
  return 0;
}
