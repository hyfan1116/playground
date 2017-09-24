
/*
 * Complete the function below.
 */
int totalRuns(vector <int> batterSpeedLimits, vector < vector<int> > pitchSpeeds) {
    int hit = 0;
    for(int i = 0; i < pitchSpeeds.size(); ++i){
        for(int j = 0; j < 3; ++j){
            if(batterSpeedLimits[i] >= pitchSpeeds[i][j]){
                ++hit;
                break;
            }
        }
    }

    if(hit >= 4){
        return hit - 3;
    }
    return 0;
}
