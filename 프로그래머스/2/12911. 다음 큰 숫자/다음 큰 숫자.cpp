#include <string>
#include <vector>
#include <bitset>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n) {
    int answer = 0;
    bitset<8> b(n);
    string bn = b.to_string();
    int cnt = count(bn.begin(), bn.end(), '1');
    
    while(true){
        n++;
        bitset<8> new_b(n);
        string new_bn = new_b.to_string();
        int new_cnt = count(new_bn.begin(), new_bn.end(), '1');
        
        if(cnt == new_cnt)
            return n;
    }
    
    
    return answer;
}