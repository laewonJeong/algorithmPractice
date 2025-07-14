/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        vector<int> bin;
        while(1){
            bin.push_back(head->val);
            head= head->next;
            if(head == NULL)
                break;
        }

        int answer = 0;
        int two = 1;
        for(int i = bin.size()-1; i>=0; i--){
            answer += bin[i] * two;
            two*=2;
        }

        return answer;
    }
};