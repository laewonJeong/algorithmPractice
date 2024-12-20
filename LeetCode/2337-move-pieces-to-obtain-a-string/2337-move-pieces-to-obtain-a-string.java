class Solution {
    public boolean canChange(String start, String target) {
        int n = start.length();
        int s_cnt, t_cnt, i, j;

        s_cnt = 0; t_cnt = 0;
        for(i = 0; i< n; i++){
            if(start.charAt(i) == '_') s_cnt++;
            if(target.charAt(i) == '_') t_cnt++;
        }
        if(t_cnt != s_cnt) return false;

        j = 0;
        char target_char, start_char;
        for(i = 0; i < n; i++){
            if(target.charAt(i) == '_') continue;
            while(start.charAt(j) == '_') 
                j++;

            target_char = target.charAt(i);
            start_char = start.charAt(j);

            if(start_char != target_char)
                return false;
            else if(start_char == 'R' && j > i)
                return false;
            else if(start_char == 'L' && j < i)
                return false;
            else
                j++;

        }

        return true;
    }
}