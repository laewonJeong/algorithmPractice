#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

long long solution(string numbers) {
    long long answer = 0;
    map<string,string> num_dic = {{"zero", "0"},{"one", "1"}, {"two", "2"}, {"three", "3"}, 
                              {"four", "4"}, {"five", "5"}, {"six", "6"},
                              {"seven", "7"},{"eight", "8"},{"nine", "9"}};
                               
    string str = "";
    string result = "";
    for(auto ch:numbers){
        str+=ch;
        if(num_dic.count(str) > 0){
            result += num_dic[str];
            str = "";
        }
    }
    
    answer = stoll(result);
    
    return answer;
}