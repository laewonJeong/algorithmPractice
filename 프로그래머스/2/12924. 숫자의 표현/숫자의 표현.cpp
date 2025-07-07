#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n) {
    int answer = 0;
    int right = 2;
    int sum = 1;
    
    for(int left = 1; left < n+1; left++){
        while(sum < n && right <= n){
            sum += right;
            right++;
        }
        if(sum == n)
            answer++;
        
        sum-=left;
    }
    return answer;
}