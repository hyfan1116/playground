// you can use includes, for example:
// #include <algorithm>
#include <vector>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

void CheckAround(unsigned int i, unsigned int j, vector< vector<int> > &A, vector< vector<int> > &B);

int solution(vector< vector<int> > &A) {
    // write your code in C++14 (g++ 6.2.0)
    int ccount = 0;
    vector<int> countryList;
    int x = A[0].size();
    int y = A.size();
    vector< vector<int> > B(y,vector<int>(x));
    
    for (unsigned int i=0;i<B.size();i++){
        for (unsigned int j=0;j<B[0].size();j++){
            B[i][j] = 0;
        }    
    }
    
    for (unsigned int i=0;i<A.size();i++){
        for (unsigned int j=0;j<A[0].size();j++){
            if (B[i][j] == 0){
                ccount += 1;
                B[i][j] = ccount;
                CheckAround(i,j,A,B);
            }
        }    
    }
    
    return ccount;
}

void CheckAround(unsigned int i, unsigned int j, vector< vector<int> > &A, vector< vector<int> > &B){
    int color = A[i][j];
    int label = B[i][j];
    
    if(i>0){
        if(B[i-1][j] == 0){
            if(A[i-1][j]==color){
                B[i-1][j] = label;
                CheckAround(i-1,j,A,B);
            }
        }
    }
    if(i<A.size()-1){
        if(B[i+1][j] == 0){
            if(A[i+1][j]==color){
                B[i+1][j] = label;
                CheckAround(i+1,j,A,B);
            }
        }
    }
    if(j>0){
        if(B[i][j-1] == 0){
            if(A[i][j-1]==color){
                B[i][j-1] = label;
                CheckAround(i,j-1,A,B);
            }
        }
    }
    if(j<A[0].size()-1){
        if(B[i][j+1] == 0){
            if(A[i][j+1]==color){
                B[i][j+1] = label;
                CheckAround(i,j+1,A,B);
            }
        }
    }
}