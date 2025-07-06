class FindSumPairs {
public:
    vector<int> arr1, arr2;
    unordered_map<int, int> nums2_cnt;

    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        arr1 = nums1;
        arr2 = nums2;

        for(auto& num:arr2)
            nums2_cnt[num]++;

    }
    
    void add(int index, int val) {
        nums2_cnt[arr2[index]]--;
        nums2_cnt[arr2[index]+val]++;
        arr2[index] += val;
    }
    
    int count(int tot) {
        int result = 0;

        for(auto& num:arr1){
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