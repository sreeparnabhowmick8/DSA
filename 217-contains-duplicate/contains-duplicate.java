class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++){
            if(i==nums.length-1){
                break;
            }
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
        return false;
    }
}