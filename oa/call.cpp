// you can use includes, for example:
// #include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    // write your code in C++14 (g++ 6.2.0)
    vector<vector<string>> callList;
    stringstream sstream(S);
    string line;
    vector<string> itemList;
    map<string,int> callTime;
    map<string,int> callFee;
    
    while(getline(sstream,line,'\n')){
        //S->hh,mm,ss,pn
        itemList.push_back(line.substr(0,2));
        itemList.push_back(line.substr(3,2));
        itemList.push_back(line.substr(6,2));
        itemList.push_back(line.substr(9,11));
        callList.push_back(itemList);
        itemList.clear();
    }
    
    int feeSum = 0;
    for(unsigned int i=0;i<callList.size();i++){
        /*for(unsigned int j=0;j<callList[i].size();j++){
            cout << callList[i][j] <<endl;
        }*/
        int hh = stoi(callList[i][0]);
        int mm = stoi(callList[i][1]);
        int ss = stoi(callList[i][2]);
        string pn = callList[i][3];
        int sec;
        int min;
        int fee;
        if (hh<1 && mm<5){
            min = 0;
            sec = mm*60+ss;
            fee = sec*3;
        }
        else {
            min = hh*60+mm+(ss>0)*1;
            sec = hh*60*60+mm*60+ss;
            fee = min*150;
        }
        feeSum += fee;
        
        if (callTime.find(pn) == callTime.end()){
            callTime[pn] = sec;
            callFee[pn] = fee;
        }
        else {
            callTime[pn] += sec;
            callFee[pn] += fee;
        }
    }
    
    string maxCaller;
    int maxCallTime = 0;
    map<string,int>::iterator it;
    for(it=callTime.begin();it != callTime.end();it++){
        //cout << it->first << " " << it->second << endl;
        if (it->second > maxCallTime){
            maxCaller = it->first;
            maxCallTime = it->second;
        }
        else if (it->second == maxCallTime){
            string thisCaller = it->first;
            int thisCallerInt = stoi( thisCaller.substr(0,3) );
            int maxCallerInt = stoi( maxCaller.substr(0,3) );
            bool update = thisCallerInt < maxCallerInt;
            if (thisCallerInt == maxCallerInt){
                thisCallerInt = stoi( thisCaller.substr(4,3) );
                maxCallerInt = stoi( maxCaller.substr(4,3) );
                update = thisCallerInt < maxCallerInt;
                if (thisCallerInt == maxCallerInt){
                    thisCallerInt = stoi( thisCaller.substr(8,3) );
                    maxCallerInt = stoi( maxCaller.substr(8,3) );
                    update = thisCallerInt < maxCallerInt;
                }
            }
            
            if(update){
                maxCaller = it->first;
                maxCallTime = it->second;
            }
        }
        
    }
    
    feeSum -= callFee[maxCaller];
    
    return feeSum;
}