class Solution {
    public int maximumBeauty(int[] nums, int k) {
        Arrays.sort(nums);

        int idx = 0;

        for(int num: nums){
            if((num - nums[idx]) > 2 * k){
                idx++;
            }
        }

        return nums.length - idx;
    }
}