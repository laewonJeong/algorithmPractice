#include <string>
#include <vector>
#include <iostream>
#include <cctype>
using namespace std;

string solution(string s) {
    string answer = "";
    
    for(auto ch:s){
        if(ch < 97 && !isdigit(ch) && ch != ' '){
            ch += 32;
        }
        answer+=ch;
    } 
    
    for(int i = 0; i< answer.length(); i++){
        if(i == 0 && !isdigit(answer[i]))
            answer[i] -= 32;
        else if(answer[i-1] == ' ' && !isdigit(answer[i]) && answer[i] != ' ')
            answer[i] -= 32;
    }
    
    return answer;
}