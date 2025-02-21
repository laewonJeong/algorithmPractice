import java.util.*;

class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;
        Set<Integer> numSet = new HashSet<>();

        for (String num : nums) {
            numSet.add(Integer.parseInt(num, 2));
        }

        // 0부터 2^n - 1까지 없는 숫자 찾기
        for (int j = 0; j < (1 << n); j++) {
            if (!numSet.contains(j)) {
                return String.format("%" + n + "s", Integer.toBinaryString(j)).replace(' ', '0');
            }
        }
        return "";
    }
}