#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <regex>
#include <exception>
#include <iomanip>

using namespace std;

// too slow?

struct Log{
    string date;
    string time;
    string uri;
    string status;
    string key;
};

unordered_map<string, string> month {
    {"Jan","01"},{"Feb","02"},{"Mar","03"},{"Apr","04"},{"May","05"},{"Jun","06"},
    {"Jul","07"},{"Aug","08"},{"Sep","09"},{"Oct","10"},{"Nov","11"},{"Dec","12"}
};

vector<int> parseLogDateTime(string s){
    vector<int> dt;

    string p = R"((\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}))";
    regex r(p);
    smatch m;
    if(regex_search(s,m,r)){
        for(int i=1; i<m.size(); ++i){
            dt.push_back(stoi(m[i].str()));
        }
    }
    return dt;
}

struct {
    bool operator() (string lhs, string rhs){
        vector<int> l = parseLogDateTime(lhs);
        vector<int> r = parseLogDateTime(rhs);
        for(int i=0; i<5; ++i){
            if(l[i] != r[i]){
                return l[i] < r[i];
            }
        }
        string sl = lhs.substr(17);
        string sr = rhs.substr(17);
        return sl < sr;
    }
} log_cmp;

Log parseLog(string s){
    //cout << s << endl;
    Log l;
    string p1 = R"((\d{2})\/(\w{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2}) (\+|\-)(\d{2})(\d{2}))";
    regex r1(p1);
    smatch m1;
    if(regex_search(s,m1,r1)){
        if(m1[8].str() != "00" || m1[9].str() != "00"){
            // to GMT
            struct tm timeinfo = {0};
            timeinfo.tm_sec = stoi(m1[6].str());
            timeinfo.tm_min = stoi(m1[5].str());
            timeinfo.tm_hour = stoi(m1[4].str());
            timeinfo.tm_mday = stoi(m1[1].str());
            timeinfo.tm_mon = stoi(month[m1[2].str()])-1;
            timeinfo.tm_year = stoi(m1[3].str())-1900;
            time_t tt = mktime(&timeinfo);

            int sign = 1;
            if(m1[7].str() == "+"){
                sign = -1;
            }
            int offset = sign*(stoi(m1[8].str())*3600 + stoi(m1[9].str())*60);
            tt += offset;
            string ttt(ctime(&tt));
            l.date = ttt.substr(20, 4)+"-"+month[ttt.substr(4,3)]+"-"+ttt.substr(8,2);
            l.time = "T"+ttt.substr(11, 8);
        }
        else{
            l.date = m1[3].str()+"-"+month[m1[2].str()]+"-"+m1[1].str();
            l.time = "T"+m1[4].str()+":"+m1[5].str();
        }
        //cout << l.date+l.time << endl;
    }
    else{
        throw invalid_argument("invalid date/time");
    }

    string p2 = R"#("(GET|POST|HEAD) (.*) HTTP\/1\.1" (\d{3}))#"; //
    regex r2(p2);
    smatch m2;
    if(regex_search(s,m2,r2)){
        l.uri = m2[2].str().substr(0, m2[2].str().find('?'));
        l.status = m2[3].str();
        //cout << l.uri << ' ' << l.status << endl;
    }
    else{
        throw invalid_argument("invalid uri/status");
    }

    l.key = l.date+l.time+" "+l.uri;

    return l;
}

vector<string> calculateRates(vector<string> logs){
    unordered_map<string, pair<int,int>> stats;
    for(string log : logs){
        Log l = parseLog(log);

        if(stats.find(l.key) == stats.end()){
            stats[l.key] = make_pair(1,0);
            if(l.status[0] != '5'){
                stats[l.key].second += 1;
            }
        }
        else{
            stats[l.key].first += 1;
            if(l.status[0] != '5'){
                stats[l.key].second += 1;
            }
        }
    }

    vector<string> result;
    for(auto kv : stats){
        float rate = kv.second.second*100.0/kv.second.first;
        /*
        stringstream stream;
        stream << fixed << setprecision(2) << rate;
        string rate_str = stream.str();
        */
        string rate_str = to_string(rate);
        rate_str = rate_str.substr(0, rate_str.find('.')+3);

        result.push_back(kv.first+" "+rate_str);
    }

    sort(result.begin(), result.end(), log_cmp);
    
    return result;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    vector<string> logs;
    string tmp;
    while(getline(cin,tmp)){
        logs.push_back(tmp);
    }

    vector<string> result = calculateRates(logs);
    for(string r : result){
        cout << r << endl;
    }

    return 0;
}
