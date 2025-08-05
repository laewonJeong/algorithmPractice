#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> numbers, int k) {
    int answer = 0;
    int n = numbers.size();
    
    for(int i = 0; i< k-1; i++){
        answer += 2;
        
        if(answer >= n)
            answer %= n;
    
    }

    return numbers[answer];
}