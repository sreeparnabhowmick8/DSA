class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int minlen=1234567;
        int left=0;
        int currsum=0;
        for (int i=0;i<nums.length;i++){
            currsum=currsum+nums[i];
            while(currsum>=target){
                if(i-left+1<minlen){
                    minlen=i-left+1;
                }
                currsum=currsum-nums[left];
                left=left+1;
            }
        }
        if(minlen!=1234567){
                return minlen;
            }
            else{
            return 0;
            }
    }
}