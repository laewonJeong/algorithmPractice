#include<string>
#include <iostream>
#include <deque>
#include <vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    deque<char> dq;
    vector<char> v;
    
    for(auto ch:s)
        dq.push_back(ch);
    
    while(!dq.empty()){
        if(!v.empty() && v.back() == '(' and dq[0] == ')'){
            v.pop_back();
            dq.pop_front();
        }
        else{
            v.push_back(dq[0]);
            dq.pop_front();
        }
    }

    return v.empty();
}