#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

double findMaxCP(long numPowerUps, vector<int> pokemonArray,
  CPMultiplier CPMMapping){
  priority_queue<double> pq;

  for(int i=0; i<pokemonArray.size(); ++i){
    pq.push(pokemonArray[i]);
  }

  double result = 0;
  for(int i = 0; i < numPowerUps; ++i){

  }
  return result;
}

int main(){
  return 0;
}
