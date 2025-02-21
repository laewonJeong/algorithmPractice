import java.util.HashSet;
import java.util.Set;

class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;
        Set<String> numSet = new HashSet<>();
        
        for (String num : nums) {
            numSet.add(num);
        }

        return backtracking(new StringBuilder(), 0, n, numSet);
    }

    private String backtracking(StringBuilder now, int lenNow, int n, Set<String> numSet) {
        if (lenNow == n) {
            String binaryString = now.toString();
            return numSet.contains(binaryString) ? null : binaryString;
        }

        for (char bit : new char[]{'0', '1'}) {
            now.append(bit);
            String result = backtracking(now, lenNow + 1, n, numSet);
            if (result != null) return result;
            now.deleteCharAt(now.length() - 1); // 백트래킹 수행
        }

        return null;
    }
}
