#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    int turn = 1;
    int people = 2;
    int m = words.size();
    vector<string> check;
    
    check.push_back(words[0]);
    for(int i = 1; i<m;i++){
        if(find(check.begin(), check.end(), words[i]) == check.end() && words[i][0] == words[i-1].back()){
            check.push_back(words[i]);
            people++;
        }
        else{
            return {people, turn};
        }
        
        if(people > n){
            turn++;
            people = 1;
        }
    }

    return {0, 0};
}