class FindSumPairs {
public:
    vector<vector<int>> arr;
    unordered_map<int, int> nums2_cnt;

    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        arr.push_back(nums1);
        arr.push_back(nums2);

        for(auto num:nums2)
            nums2_cnt[num]++;

    }
    
    void add(int index, int val) {
        nums2_cnt[arr[1][index]]--;
        nums2_cnt[arr[1][index]+val]++;
        arr[1][index] += val;
    }
    
    int count(int tot) {
        int result = 0;

        for(auto num:arr[0]){
            if(nums2_cnt[tot-num] != 0)
                result += nums2_cnt[tot-num];
        }
        return result;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */