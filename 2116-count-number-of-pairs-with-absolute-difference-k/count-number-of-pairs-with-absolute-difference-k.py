class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # diff=-123456
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff=abs(nums[i]-nums[j])
                if(diff==k):
                    count+=1
        return count            
        