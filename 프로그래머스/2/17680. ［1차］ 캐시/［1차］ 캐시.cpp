#include <string>
#include <vector>
#include <unordered_map>
#include <list>
#include <cctype>

using namespace std;

string to_lower(const string& s) {
    string res;
    for (char ch : s) res += tolower(ch);
    return res;
}

int solution(int cacheSize, vector<string> cities) {
    if (cacheSize == 0) return 5 * cities.size();
    
    int answer = 0;
    list<string> cache;  // 순서를 위한 리스트
    unordered_map<string, list<string>::iterator> cache_map;

    for (string city_raw : cities) {
        string city = to_lower(city_raw);
        
        // 캐시 히트
        if (cache_map.find(city) != cache_map.end()) {
            answer += 1;
            // 캐시 순서 갱신: 삭제 후 push_back
            cache.erase(cache_map[city]);
        } else {
            answer += 5;
            if (cache.size() == cacheSize) {
                string lru = cache.front();
                cache.pop_front();
                cache_map.erase(lru);
            }
        }
        cache.push_back(city);
        cache_map[city] = prev(cache.end());
    }

    return answer;
}
