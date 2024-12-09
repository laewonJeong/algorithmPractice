class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        int qn = queries.length;
        boolean[] answer = new boolean[qn];
        List<int[]> falseList = new ArrayList<>();


        for(int i = 0; i < n-1; i++){
            if ((nums[i] % 2 == 0 && nums[i+1] % 2 == 0) || (nums[i] % 2 != 0 && nums[i+1] % 2 != 0)){
                falseList.add(new int[]{i, i+1});
            }
        }
        
        for(int i = 0; i < qn; i++){
            int left = 0;
            int right = falseList.size()-1;
            boolean check = true;

            while (left <= right){
                int mid = (left+right)/2;
                if (queries[i][0] <= falseList.get(mid)[0] && falseList.get(mid)[0] <= queries[i][1] && 
                    queries[i][0] <= falseList.get(mid)[1] && falseList.get(mid)[1] <= queries[i][1]) {
                        check = false;
                        break;
                }
                else if (falseList.get(mid)[1] <= queries[i][0]){
                    left = mid+1;
                }
                else{
                    right = mid-1;
                }
            }
            answer[i] = check;

        }

        return answer;
    }
}