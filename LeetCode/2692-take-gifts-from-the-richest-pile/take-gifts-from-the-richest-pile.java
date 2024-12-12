class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> pQ = new PriorityQueue<>(Collections.reverseOrder());

        for(int gift: gifts){
            pQ.add(gift);
        }

        for(int i = 0; i < k; i++){
            int maxGift = (int)Math.sqrt(pQ.poll());
            pQ.add(maxGift);
        }

        return sumOperation(pQ);
    }

    private long sumOperation(PriorityQueue<Integer> pQ){
        long sum = 0;
        
        for(int num: pQ){
            sum += num;
        }

        return sum;
    }
}