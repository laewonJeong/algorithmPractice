#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> numbers) {
    sort(numbers.begin(), numbers.end());
    int answer = numbers.back();
    numbers.pop_back();
    
    return answer * numbers.back();
}