
class Solution:
    import math
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # brute force
        # for i in range(1,max(nums)+1):
        #     sum1=0
        #     for j in range(len(nums)):
        #         sum1+=math.ceil(nums[j]/i)
        #     if(sum1<=threshold):
        #         return i
        # return -1 
        # binary search
        def result(mid,nums):
            sum1=0
            for i in range(len(nums)):
                sum1+=math.ceil(nums[i]/mid) 
            return sum1    
        low,high=1,max(nums)
        ans=0
        while(low<=high):
            mid=int((low+high)/2)
            if(result(mid,nums)<=threshold):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans                      
        