#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
    string answer = "";
    string temp = "";
    vector<int> num;
    
    for(auto ch:s){
        if(ch != ' ')
            temp+=ch;
        else{
            num.push_back(stoi(temp));
            temp = "";
        }
    }
    num.push_back(stoi(temp));
    
    int max_num = *max_element(num.begin(), num.end());
    int min_num = *min_element(num.begin(), num.end());
    
    answer = to_string(min_num) + " " + to_string(max_num);
    return answer;
}