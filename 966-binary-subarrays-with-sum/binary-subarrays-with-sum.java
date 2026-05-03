class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        return helper(nums,goal)-helper(nums,goal-1);
    }
    public  int helper(int[] nums,int goal){
            int l=0,r=0,count=0,sum=0;
            int n=nums.length;
            while(r<n){
                 sum+=nums[r];
                 while(sum>goal && l<=r){
                    sum-=nums[l];
                    l+=1;
                 }
                 if(sum<=goal){
                    count+=(r-l+1);
                 }
                 r+=1;              
            }
            return count;
        }
}