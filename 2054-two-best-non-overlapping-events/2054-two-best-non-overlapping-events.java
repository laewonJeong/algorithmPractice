class Solution {
    public int maxTwoEvents(int[][] events) {
        int answer = 0;
        
        Arrays.sort(events, (a,b) -> a[0] - b[0]);
        int n = events.length;
        
        int[] maxValue = new int[n];
        
        maxValue[n-1] = events[n-1][2];
        
        for(int i = n - 2; i >= 0; i--){
            maxValue[i] = Math.max(events[i][2], maxValue[i+1]);
        }
        
        int left, right, mid, idx;
        
        for(int i = 0; i < n; i++){
            //System.out.println(answer);
            answer = Math.max(answer, events[i][2]);
            left = 0;
            right = n-1;
            idx = -1;
            
            while(left <= right){
                mid = (left+right)/2;
                
                if(events[mid][0] > events[i][1]){
                    right = mid -1;
                    idx = mid;
                }
                else{
                    left = mid + 1;
                }
            }
            if(idx != -1){
                answer = Math.max(answer, events[i][2] + maxValue[idx]);
            }
            
        }
        
        return answer;
    }
}