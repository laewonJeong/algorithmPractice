import java.util.*;

class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;

        int[] arr = new int[n];

        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(nums[i], 2);
        }
        Arrays.sort(arr);

        int maxN = (int) Math.pow(2, n);

        int i = 0;
        int j = 0;
        while(j <= maxN && i < n) {
            System.out.println(arr[i] + " " + j);

            if(arr[i] == j) {
                i++;
                j++;
            } 
            else {

                return String.format("%0"+n+"d", Integer.parseInt(Integer.toBinaryString(j)));
            }
        }
        return String.format("%0"+n+"d", Integer.parseInt(Integer.toBinaryString(j)));
    }
}